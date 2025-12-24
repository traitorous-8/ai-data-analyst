import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import matplotlib.pyplot as plt
from llm import analyze_dataframe
from visualize.plotter import plot_column, plot_pie, plot_line, plot_auto

load_dotenv()

st.title("AI Data Analyst")

uploaded_file = st.file_uploader(
    "Выберите CSV или Excel файл", type=["csv", "xlsx", "xls"]
)

user_prompt = st.text_input("Введите зарос к данным")

if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    if user_prompt.strip():
        st.subheader("Анализ от LLM")
        analysis = analyze_dataframe(df, user_prompt)
        st.write(analysis)

    st.subheader("Данные")
    st.dataframe(df.head())

    columns = st.multiselect("Выберите колонку(и) для графика", df.columns)

    graph_type = st.selectbox(
        "Выберите тип графика", ["Авто", "Бар", "Круг", "Линейный"]
    )

    for column in columns:
        st.write(f"### График для колонки: {column}")
        plt.figure()

        if graph_type == "Бар":
            plot_column(df, column)
        elif graph_type == "Круг":
            plot_pie(df, column)
        elif graph_type == "Линейный":
            plot_line(df, column)
        else:
            plot_auto(df, column)

        st.pyplot(plt.gcf())
        plt.close()
