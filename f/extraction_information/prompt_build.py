import wmill
from typing import Optional


# mapping prompt resource
PROMPT_REGISTRY = {
    "phieu_chi": "f/extraction_information/phieu_chi",
    "phieu_thu": "f/extraction_information/phieu_thu",
    "default": "f/extraction_information/prompt_default",
}


def detect_doc_type(user_prompt: Optional[str]) -> str:
    """
    Chỉ detect từ user_prompt
    KHÔNG dùng OCR để tránh sai logic
    """

    if not user_prompt:
        return "default"

    text = user_prompt.lower()

    if "phiếu chi" in text:
        return "phieu_chi"

    if "phiếu thu" in text:
        return "phieu_thu"

    return "default"


def build_prompt(user_prompt: Optional[str], ocr_text: str):
    """
    Build prompt theo logic:
    - Nếu user có prompt → chọn prompt tương ứng
    - Nếu không → dùng default
    - Luôn kết hợp user_prompt + system_prompt
    """

    # 1. detect loại phiếu (CHỈ từ user_prompt)
    doc_type = detect_doc_type(user_prompt)

    # 2. lấy system prompt từ resource
    prompt_path = PROMPT_REGISTRY.get(doc_type, PROMPT_REGISTRY["default"])
    system_prompt = wmill.get_resource(prompt_path)

    # fallback nếu resource lỗi
    if not system_prompt:
        system_prompt = ""

    # 3. build prompt cuối
    final_prompt = f"""
{system_prompt}

---------------------
NGỮ CẢNH NGƯỜI DÙNG:
{user_prompt if user_prompt else "Không có"}

---------------------
DỮ LIỆU OCR:
{ocr_text}

---------------------
YÊU CẦU:
- Nếu user có chỉ định → ưu tiên theo user
- Nếu không → xử lý tổng quát
- Chỉ trả về JSON hợp lệ
- Không giải thích
- Giữ nguyên ngôn ngữ gốc (ưu tiên tiếng Việt)
- KHÔNG viết code
- KHÔNG giải thích
- KHÔNG markdown
- KHÔNG ```python
- KHÔNG ```json
- KHÔNG text thừa
- Output phải parse được bằng json.loads()

Nếu sai format → coi như thất bại
"""

    return final_prompt, doc_type