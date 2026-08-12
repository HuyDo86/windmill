from f.extraction_information.utils import (
    parse_input_text,
    extract_json,
    clean_extracted_data,
    compute_accuracy_score,
)

from f.extraction_information.prompt_builder_core import build_prompt
from f.extraction_information.model_loader_core import get_model_config
from f.extraction_information.llm_core import call_llm
from f.extraction_information.schema_loader_core import get_schema


def run_extraction(
    file_content,
    doc_type: str,
    model_path: str | None = None,
    prompt_path: str | None = None,
):
    # 1. OCR
    ocr_text = parse_input_text(file_content)

    # 2. PROMPT
    prompt = build_prompt(ocr_text, prompt_path)

    # 3. MODEL
    model_cfg = get_model_config(model_path)

    print("MODEL CFG:", model_cfg)

    # 4. CALL LLM
    raw_output = call_llm(model_cfg, prompt)

    print("RAW OUTPUT:", raw_output)

    # 5. PARSE JSON
    data = extract_json(raw_output)

    if not data:
        data = {
            "raw_output": raw_output,
            "error": "empty_json",
        }

    # 6. CLEAN
    data = clean_extracted_data(data)

    # 7. LOAD SCHEMA (SYSTEM)
    schema = get_schema(doc_type)

    return {
        "document_type": doc_type,
        "extracted_data": data
    }