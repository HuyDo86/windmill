import wmill
import textwrap

PROMPT_DEFAULT_PATH = "f/extraction_information/prompt_default"


def build_prompt(
    ocr_text: str,
    prompt_path: str | None,
):

    # LOAD PROMPT

    try:
        if prompt_path:
            system_prompt = wmill.get_resource(prompt_path)
        else:
            system_prompt = wmill.get_resource(PROMPT_DEFAULT_PATH)
    except Exception as e:
        print("Load prompt failed:", e)
        system_prompt = ""


    # BUILD FINAL PROMPT
    
    final_prompt = textwrap.dedent(
        f"""
{system_prompt}

---------------------
DỮ LIỆU OCR:
{ocr_text}

---------------------
YÊU CẦU:
- CHỈ trả về JSON hợp lệ
- KHÔNG giải thích
- KHÔNG code
- KHÔNG markdown
"""
    ).strip()

    return final_prompt