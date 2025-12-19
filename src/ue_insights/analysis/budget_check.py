def apply_budgets(df, budgets: dict):
    df = df.copy()
    df["budget_ms"] = df["Name"].map(budgets)
    df["over_budget_ms"] = df["frame_time_ms"] - df["budget_ms"]
    df["over_budget"] = df["over_budget_ms"] > 0
    return df
