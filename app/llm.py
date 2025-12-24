import os
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask_llm(df: pd.DataFrame, user_prompt: str) -> str:
    """
    Анализирует Табличные данные с помощью OpenAI LLM
    """

    preview = df.head(20).to_string()

    system_prompt = (
        "Ты Senior Data Analyst."
        "Твоя задача - анализировать предоставленные данные."
        "НЕ пиши код."
        "НЕ предлагай примеры кода."
        "Делай вывод ТОЛЬКО на основе данных."
        "Пиши кртако, списками."
    )

    user_message = f"""
Вот пример данных (первые строки):
{preview}

Запрос пользователя:
{user_prompt}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
        max_tokens=400,
        temperature=0.4,
    )

    return response.choices[0].message.content
