import wmill
from typing import Optional
from f.extraction_information.core.main_core import run_extraction


def main(
    file_content: bytes,
    prompt_path: Optional[str] = None,
    model_path: Optional[str] = None,
):
    return run_extraction(
        file_content=file_content,
        doc_type="bien_ban_lam_viec",
        model_path=model_path,
        prompt_path=prompt_path,
    )