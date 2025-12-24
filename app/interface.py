import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from data.loader import load_file
from visualize.plotter import plot_column, plot_pie, plot_line, plot_auto
from llm import ask_llm
import matplotlib.pyplot as plt


def run_app():
    load_dotenv()

    st.set_page_config(page_title="AI Data Analyst", layout="wide")
    st.title("AI Data Analyst")

    uploaded_file = st.file_uploader(
        "Загрузите CSV или Excel файл", type=["csv", "xlsx", "xls"]
    )
    if uploaded_file is None:
        st.info("Пожалуйста, загрузите файл для начала анализа")
        return

    df = load_file(uploaded_file)

    st.write("### Анализ с помощью LLM")
    user_prompt = st.text_area(
        "Введите запрос к данным (например: 'Проанализируйте респределение рейтинигов)"
    )

    if st.button("Запустить анализ"):
        with st.spinner("LLM анализирует данные..."):
            response = ask_llm(df, user_prompt)
        st.success("Готово!")
        st.write(response)

    st.write("### Визуализация")

    columns = st.multiselect("Выберите колонку (и) для графика", df.columns)
    graph_type = st.selectbox(
        "Выберите тип графика", ["Авто", "Бар", "Круг", "Линейный"]
    )

    if not columns:
        st.info("Выберите колонку для построения графика")
        return

    for column in columns:
        st.write(f"#### График для колонки: {column}")
        plt.figure()

    try:
        if graph_type == "Бар":
            plot_column(df, column)
        elif graph_type == "Круг":
            plot_pie(df, column)
        elif graph_type == "Линейный":
            plot_line(df, column)
        else:
            plot_auto(df, column)

        st.pyplot(plt.gcf())
    except Exception as e:
        st.error(f"Невозможно построить график для колонки '{column}")
    finally:
        plt.close()
