import pandas as pd
import matplotlib.pyplot as plt


def plot_column(df, column):
    plt.figure(figsize=(8, 5))
    df[column].value_counts().plot(kind="bar")
    plt.title(f"Распределение значений: {column}")
    plt.xlabel("Значение")
    plt.ylabel("Количество")
    plt.tight_layout()


def plot_pie(df, column):
    plt.figure(figsize=(6, 6))
    data = df[column].value_counts()
    plt.pie(data, labels=data.index, autopct="%1.1f%%", startangle=90)
    plt.title(f"Круговая диаграмма: {column}")
    plt.tight_layout()


def plot_line(df, column):
    plt.figure(figsize=(8, 5))
    plt.plot(df[column].values)
    plt.title(f"Линейный график: {column}")
    plt.xlabel("Индекс")
    plt.ylabel(column)
    plt.tight_layout()


def plot_auto(df, column):
    if pd.api.types.is_numeric_dtype(df[column]):
        plot_line(df, column)

    elif pd.api.types.is_object_dtype(df[column]):
        if df[column].nunique() <= 5:
            plot_pie(df, column)
        else:
            plot_column(df, column)

    else:
        print("Невозможно определить тип графика для этой колонки")
