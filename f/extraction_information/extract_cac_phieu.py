import os
import wmill
from typing import Literal, Optional
from f.extraction_information.main_new import run_extraction

def main(
    file_content:bytes,
    user_prompt: Optional[str] = None,

    # dropdown model
    model_name: Literal["llama", "qwen_vlm", "gpt", "deepseek"] = "qwen_vlm",


    ):
    return run_extraction(
        file_content=file_content,
        user_prompt=user_prompt,
        model_name=model_name,
    )