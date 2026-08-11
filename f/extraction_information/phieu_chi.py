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
from typing import Optional, List, Union, Any, Literal
from pydantic import BaseModel, ConfigDict
import base64
VN_TZ = timezone(timedelta(hours=7))


from f.extraction_information.main import run_extraction
from f.extraction_information.schema_class import PhieuChi


def main(
    file_content,
    user_prompt: Optional[str] = None,
    model_name: Literal["llama", "qwen_vlm", "gpt", "deepseek"] = "qwen_vlm",
):
    return run_extraction(
        file_content=file_content,
        user_prompt=user_prompt,
        model_name=model_name,
        schema_class=PhieuChi,   
    )

