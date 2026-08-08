# requirements:
# openai==1.54.0
# wmill
# httpx==0.27.2
# pydantic==2.9.0

import wmill
import os
import json
import re
from datetime import datetime, timezone, timedelta
from openai import OpenAI
from typing import Optional, List, Union, Any
from pydantic import BaseModel, ConfigDict
import base64
VN_TZ = timezone(timedelta(hours=7))


class PaymentRequestItem(BaseModel):
    model_config = ConfigDict(extra="allow")
    code: Optional[str] = None
    description: Optional[str] = None
    amount: Optional[float] = None
    attached_doc: Optional[str] = None


class PaymentRequest(BaseModel):
    model_config = ConfigDict(extra="allow")
    request_number: Optional[str] = None
    date: Optional[str] = None
    requester_name: Optional[str] = None
    requester_department: Optional[str] = None
    requester_organization: Optional[str] = None
    requester_phone: Optional[str] = None
    beneficiary_name: Optional[str] = None
    beneficiary_account: Optional[str] = None
    beneficiary_bank: Optional[str] = None
    reason: Optional[str] = None
    expense_category: Optional[str] = None
    project: Optional[str] = None
    contract: Optional[str] = None
    invoice: Optional[str] = None
    items: Optional[List[PaymentRequestItem]] = None
    total_amount: Optional[float] = None
    currency: Optional[str] = None
    total_amount_in_words: Optional[str] = None
    advance_amount: Optional[float] = None
    remaining_amount: Optional[float] = None
    approver_name: Optional[str] = None
    attached_documents: Optional[str] = None
    note: Optional[str] = None


PROMPT_TEMPLATE = """
You are an expert in OCR extraction for business documents in Vietnam.

Your task is to read the OCR input text and return a JSON object containing only the fields that are explicitly present in that OCR text.

Important rules:
1. Do not rely on a fixed schema for every document. The output schema must be dynamic.
2. Only include keys that exist in the OCR text. If a field is absent, omit it entirely.
3. Do not output null, empty strings, or placeholders such as "N/A" for missing fields.
4. Preserve the original exact values from the OCR text as much as possible.
5. If the OCR contains a table/list, keep repeated rows under an `items` list only when the OCR clearly shows such repeat rows.
6. If you see extra/custom fields not in the standard template, add them with descriptive keys.
7. Return valid JSON only. No markdown, no explanation.

Document type: yeu_cau_thanh_toan
Current date and time: {date_time}

Input text from OCR:
----------------
{ocr_text}
----------------

Your Response:
"""

def _normalize_text_value(value: Any) -> str:
    if not isinstance(value, str):
        return ""

    text = value.strip()
    if not text:
        return ""

    if text.startswith("{") and text.endswith("}"):
        try:
            payload = json.loads(text)
            if isinstance(payload, dict):
                for key in [
                    "markdown_text",
                    "ocr_input_text",
                    "text",
                    "content",
                    "raw_output",
                ]:
                    if key in payload and isinstance(payload[key], str):
                        return _normalize_text_value(payload[key])
        except Exception:
            pass

    if re.fullmatch(r"[A-Za-z0-9+/=\-\r\n]+", text) and len(text) >= 20:
        try:
            decoded_bytes = base64.b64decode(text, validate=True)
            decoded_text = decoded_bytes.decode("utf-8", errors="ignore").strip()
            if decoded_text:
                return _normalize_text_value(decoded_text)
        except Exception:
            pass

    return text

def parse_input_text(file_content: Union[bytes, str, dict]) -> str:
    if file_content is None:
        return ""
    if isinstance(file_content, bytes):
        for encoding in ["utf-8-sig", "utf-8", "utf-16", "latin-1"]:
            try:
                text = file_content.decode(encoding)
                break
            except Exception:
                continue
        else:
            text = file_content.decode("utf-8", errors="ignore")
    elif isinstance(file_content, dict):
        for key in ["markdown_text", "ocr_input_text", "text", "content", "raw_output"]:
            if key in file_content and isinstance(file_content[key], str):
                return _normalize_text_value(file_content[key])
        return _normalize_text_value(json.dumps(file_content, ensure_ascii=False))
    else:
        text = str(file_content)

    text = text.strip()
    if os.path.exists(text) and os.path.isfile(text):
        try:
            with open(text, "r", encoding="utf-8", errors="ignore") as f:
                file_str = f.read().strip()
                if file_str:
                    text = file_str
        except Exception:
            pass

    return _normalize_text_value(text)


def extract_json(raw_text: str) -> dict:
    cleaned = re.sub(r"```json\s*|\s*```", "", raw_text).strip()
    match = re.search(r"\{.*\}", cleaned, re.DOTALL)
    if match:
        cleaned = match.group(0)
    return json.loads(cleaned)


def clean_extracted_data(data: Any) -> Any:
    if isinstance(data, dict):
        cleaned = {}
        for k, v in data.items():
            if v is None:
                continue
            if isinstance(v, (dict, list)):
                cv = clean_extracted_data(v)
                if cv or cv == 0 or cv is False:
                    cleaned[k] = cv
            else:
                cleaned[k] = v
        return cleaned
    elif isinstance(data, list):
        cleaned_list = []
        for item in data:
            if item is None:
                continue
            if isinstance(item, (dict, list)):
                ci = clean_extracted_data(item)
                if ci or ci == 0 or ci is False:
                    cleaned_list.append(ci)
            else:
                cleaned_list.append(item)
        return cleaned_list
    return data


def compute_accuracy_score(ocr_text: str, extracted_data: Any) -> float:
    if not isinstance(ocr_text, str) or not ocr_text.strip():
        return 0.0

    ocr_norm = re.sub(r"\s+", " ", ocr_text).strip().lower()
    if not ocr_norm:
        return 0.0

    def walk(value: Any) -> tuple[int, int]:
        matched = 0
        total = 0
        if isinstance(value, dict):
            for key, item in value.items():
                if isinstance(item, (dict, list)):
                    sub_matched, sub_total = walk(item)
                    matched += sub_matched
                    total += sub_total
                elif item is not None and str(item).strip():
                    total += 1
                    key_text = str(key).lower()
                    item_text = str(item).lower()
                    if key_text in ocr_norm or item_text in ocr_norm:
                        matched += 1
        elif isinstance(value, list):
            for item in value:
                sub_matched, sub_total = walk(item)
                matched += sub_matched
                total += sub_total
        return matched, total

    matched, total = walk(extracted_data)
    if total == 0:
        return 0.0
    return round((matched / total) * 100.0, 2)


def main(
    file_content: Union[bytes, str, dict],
    vlm_resource: dict = wmill.get_resource("u/huyxuan264/qwen_vlm"),
) -> dict:

    markdown_text = parse_input_text(file_content)

    extract_start = datetime.now(VN_TZ)

    prompt = PROMPT_TEMPLATE.format(
        date_time=extract_start.strftime("%Y-%m-%d %H:%M:%S"),
        ocr_text=markdown_text,
    )

    client = OpenAI(
        api_key=vlm_resource["api_key"],
        base_url=vlm_resource["base_url"],
    )

    response = client.chat.completions.create(
        model=vlm_resource.get("model", "5CD-AI/Vintern-3B-R-beta"),
        messages=[{"role": "user", "content": prompt}],
        max_tokens=4000,
        temperature=0.0,
    )
    raw_output = response.choices[0].message.content
    extract_end = datetime.now(VN_TZ)

    try:
        parsed_json = extract_json(raw_output)
        extracted_data = clean_extracted_data(parsed_json)
        if not isinstance(extracted_data, dict):
            extracted_data = {"raw_output": raw_output}
    except json.JSONDecodeError:
        extracted_data = {"raw_output": raw_output}

    return {
        "document_type": "yeucauthanhtoan",
        "extracted_data": extracted_data,
        "extract_duration_seconds": round(
            (extract_end - extract_start).total_seconds(), 2
        ),
        "extraction_accuracy_score": compute_accuracy_score(
            markdown_text, extracted_data
        ),
    }
