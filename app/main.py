import pandas as pd


def load_file(path: str):
    if path.endswith(".csv"):
        return pd.read_csv(path)
    elif path.endswith(".xlsx") or path.endswith(".xls"):
        return pd.read_excel(path)
    else:
        raise ValueError("Неподдерживаемый формат файла")


def get_basic_info(df: pd.DataFrame):
    return {
        "rows": df.shape[0],
        "columns": list(df.columns),
        "shape": df.shape,
        "drypes": df.dtypes.astype(str).to_dict(),
    }


def get_statistics(df: pd.DataFrame):
    return df.describe(include="all")
