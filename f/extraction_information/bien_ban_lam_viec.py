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

from f.extraction_information.utils import (
    _normalize_text_value,
    parse_input_text,
    extract_json,
    clean_extracted_data,
    compute_accuracy_score,
)
from f.extraction_information.schema import BienBanLamViec
from f.extraction_information.prompt import build_prompt
from f.extraction_information.main import run_extraction


def main(file_content: bytes):

    return run_extraction(
        file_content=file_content,
        parse_input_text=parse_input_text,
        build_prompt=build_prompt,
        extract_json=extract_json,
        clean_extracted_data=clean_extracted_data,
        compute_accuracy_score=compute_accuracy_score,
        document_type="Biên bản làm việc",
        model="5CD-AI/Vintern-3B-R-beta",
        schema=BienBanLamViec,
    )