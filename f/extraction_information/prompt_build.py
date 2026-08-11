import wmill


PROMPT_REGISTRY = {
    "phieu_chi": "f/extraction_information/phieu_chi",
    "phieu_thu": "f/extraction_information/phieu_thu",
    "default": "f/extraction_information/default",
}


def detect_doc_type(user_prompt: str | None, ocr_text: str) -> str:
    text = (user_prompt or "") + " " + ocr_text.lower()

    if "phiếu chi" in text:
        return "phieu_chi"
    if "phiếu thu" in text:
        return "phieu_thu"

    return "default"


def build_prompt(user_prompt: str | None, ocr_text: str):
    doc_type = detect_doc_type(user_prompt, ocr_text)

    system_prompt = wmill.get_resource(
        PROMPT_REGISTRY.get(doc_type, PROMPT_REGISTRY["default"])
    )

    final_prompt = f"""
{system_prompt}

---------------------
YÊU CẦU NGƯỜI DÙNG:
{user_prompt or "Không có"}

---------------------
DỮ LIỆU OCR:
{ocr_text}

---------------------
Chỉ trả về JSON hợp lệ.
Không giải thích.
Giữ nguyên ngôn ngữ gốc (ưu tiên tiếng Việt).
"""

    return final_prompt, doc_type