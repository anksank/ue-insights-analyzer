def normalize_to_ms(df, frame_count: int):
    df = df.copy()
    df["frame_time_ms"] = (df["Incl"] * 1000) / frame_count
    return df
