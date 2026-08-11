import os
import wmill
from typing import Optional, Literal

from f.extraction_information.utils import (
    parse_input_text,
    extract_json,
    clean_extracted_data,
    compute_accuracy_score,
)
from f.extraction_information.prompt_build import build_prompt
from f.extraction_information.model_loader import get_model_config
from f.extraction_information.llm import call_llm
from f.extraction_information.schema import SCHEMA_REGISTRY 


def run_extraction(
    file_content,
    user_prompt: Optional[str] = None,
    model_name: Literal["llama", "qwen_vlm", "gpt", "deepseek"] = "qwen_vlm",
):
    # 1. OCR
    ocr_text = parse_input_text(file_content)

    # 2. Prompt + detect doc_type
    prompt, doc_type = build_prompt(user_prompt, ocr_text)

    # 3. Load model
    model_cfg = get_model_config(model_name)

    # 4. Call LLM
    raw_output = call_llm(model_cfg, prompt)

    # 5. Parse JSON
    try:
        data = extract_json(raw_output)
    except:
        data = {"raw_output": raw_output}

    # 6. Clean
    data = clean_extracted_data(data)

    # 7. Map schema tự động
    schema_class = SCHEMA_REGISTRY.get(doc_type)

    if schema_class:
        try:
            data = schema_class(**data).dict()
        except Exception as e:
            print("Schema validate failed:", e)

    # 8. Accuracy
    accuracy = compute_accuracy_score(ocr_text, data)

    return {
        "document_type": doc_type,
        "extracted_data": data,
        "accuracy": accuracy,
    }