import os
import wmill
from openai import OpenAI


def call_llm(model_cfg, prompt):
    client = OpenAI(
        api_key=model_cfg["api_key"],
    )

    res = client.chat.completions.create(
        model=model_cfg["model"],
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=4000,
    )

    return res.choices[0].message.content