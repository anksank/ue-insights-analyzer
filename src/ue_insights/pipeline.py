from .io.csv_loader import load_trace_csv
from .analysis.normalize import normalize_to_ms
from .analysis.budget_check import apply_budgets
from .model.summary import TraceSummary
from .model.events import EventTiming
from .llm.prompt_builder import build_prompt

def run_pipeline(
    csv_path,
    frame_count,
    budgets,
    previous_summary=None,
    llm_client=None,
    device_profile="unknown",
    fps_target=0,
):
    df = load_trace_csv(csv_path)
    df = normalize_to_ms(df, frame_count)
    df = apply_budgets(df, budgets)

    violations = df[df["over_budget"]].sort_values(
        "over_budget_ms", ascending=False
    )

    top_violations = []
    for _, row in violations.iterrows():
        top_violations.append(
            EventTiming(
                name=row["Name"],
                frame_time_ms=row["frame_time_ms"],
                budget_ms=row["budget_ms"],
                over_budget_ms=row["over_budget_ms"],
            )
        )

    summary = TraceSummary(
        device_profile=device_profile,
        fps_target=fps_target,
        top_violations=top_violations,
        regressions={},
        improvements={},
    )

    if llm_client:
        prompt = build_prompt(summary)
        report = llm_client.generate(prompt)
        return summary, report

    return summary, None
