import pandas as pd

def load_trace_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, encoding="utf-16")
    df["Name"] = df["Name"].str.strip()
    return df
