import os
import wmill
import json
from datetime import datetime, timezone, timedelta
from typing import Union, Any, Dict, Optional, Type
from openai import OpenAI
from f.extraction_information.utils import (
    _normalize_text_value,
    parse_input_text,
    extract_json,
    clean_extracted_data,
    compute_accuracy_score,
)
VN_TZ = timezone(timedelta(hours=7))






def run_extraction(
    file_content: Union[bytes, str, dict],
    parse_input_text,
    build_prompt,
    extract_json,
    clean_extracted_data,
    compute_accuracy_score,
    document_type: str,
    model: Optional[str] = None,
    schema: Optional[Type] = None,   
    vlm_resource: dict = wmill.get_resource("u/huyxuan264/qwen_vlm"),
) -> Dict[str, Any]:

    # 1. Parse OCR
    markdown_text = parse_input_text(file_content)

    extract_start = datetime.now(VN_TZ)

    # 2. Build prompt
    prompt = build_prompt(
        document_type=document_type,
        ocr_text=markdown_text,
        date_time=extract_start.strftime("%Y-%m-%d %H:%M:%S"),
    )

    # 3. Init client
    client = OpenAI(
        api_key=vlm_resource["api_key"],
        base_url=vlm_resource["base_url"],
    )

    # 👇 cho phép override model từ ngoài
    model_name = model or vlm_resource.get("model", "5CD-AI/Vintern-3B-R-beta")

    # 4. Call LLM
    response = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=4000,
        temperature=0.0,
    )

    raw_output = response.choices[0].message.content
    extract_end = datetime.now(VN_TZ)

    # 5. Parse JSON
    try:
        parsed_json = extract_json(raw_output)
        extracted_data = clean_extracted_data(parsed_json)

        if not isinstance(extracted_data, dict):
            extracted_data = {"raw_output": raw_output}

    except json.JSONDecodeError:
        extracted_data = {"raw_output": raw_output}

    # 6. Validate bằng schema (nếu có)
    validated_data = None
    validation_error = None

    if schema and isinstance(extracted_data, dict):
        try:
            validated_data = schema(**extracted_data).model_dump(exclude_none=True)
        except Exception as e:
            validation_error = str(e)

    # 7. Return
    return {
        "document_type": document_type,
        "model_used": model_name,
        "extracted_data": extracted_data,
        "extract_duration_seconds": round(
            (extract_end - extract_start).total_seconds(), 2
        ),
        "extraction_accuracy_score": compute_accuracy_score(
            markdown_text, extracted_data
        ),
    }