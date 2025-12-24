import pandas as pd
import matplotlib.pyplot as plt


def plot_column(df: pd.DataFrame, column: str):
    counts = df[column].value_counts().head(20)

    if counts.empty:
        raise ValueError("Недостачно данных для графика.")
    counts.plot(kind="bar")
    plt.xlabel(column)
    plt.ylabel("Количество")
    plt.tight_layout()


def plot_pie(df: pd.DataFrame, column: str):
    counts = df[column].value_counts().head(10)

    if counts.empty:
        raise ValueError("Недостачно данных для круговой диаграммы.")
    counts.plot(kind="pie", autopct="%1.1f%%", startangle=90)
    plt.ylabel("")
    plt.tight_layout()


def plot_line(df: pd.DataFrame, column: str):
    """Линейный график (для числовых данных)"""
    df[column].dropna().plot(kind="line")
    plt.xlabel("Индекс")
    plt.ylabel(column)
    plt.tight_layout()


def plot_auto(df: pd.DataFrame, column: str):
    """Автоматический выбор графика:
    - числовые данные -> линейный
    - категориальные -> столбчатый"""
    if pd.api.types.is_numeric_dtype(df[column]):
        plot_line(df, column)
    else:
        plot_column(df, column)
