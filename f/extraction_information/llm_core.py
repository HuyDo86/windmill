from openai import OpenAI


def call_llm(model_cfg, prompt):
    client = OpenAI(
        api_key=model_cfg.get("api_key"),
        base_url=model_cfg.get("base_url"),  
    )

    response = client.chat.completions.create(
        model=model_cfg.get("model"),
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=4000,
    )

    return response.choices[0].message.content