import os
import wmill
from typing import Optional
from f.extraction_information.main_new import run_extraction


def main(
    file_content,
    user_prompt: Optional[str] = None,


    model_name: Optional[str] = None,
    model_registry_url: str = "u/huyxuan264/models",
    prompt_registry_url: str = "u/huyxuan264/prompts",
):
    return run_extraction(
        file_content=file_content,
        user_prompt=user_prompt,
        model_name=model_name,
        model_registry_url=model_registry_url,
        prompt_registry_url=prompt_registry_url,
    )