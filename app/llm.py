import os
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_dataframe(df: pd.DataFrame, user_prompt: str) -> str:
    """
    Анализирует DataFrame с помощью OpenAI API
    """

    preview = df.head(20).to_string()

    system_prompt = (
        "Ты опытный аналитик данных."
        "Ты умеешь кратко и понятно объяснять структуру данных,"
        "находить интересные закономерности и предлагать идеи для графиков."
    )

    full_prompt = f"""
Вот пример данных (первые строки):
{preview}

Запрос пользователя:
{user_prompt}

Дай:
1) краткий анализ данных
2) интересные наблюдения
3) идеи для визуализаций
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": full_prompt},
        ],
        max_tokens=400,
        temperature=0.4,
    )

    return response.choices[0].message.content
