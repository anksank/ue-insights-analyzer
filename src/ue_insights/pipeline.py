from .analysis.normalize import normalize_to_ms
from .analysis.budget_check import apply_budgets
from .model.summary import TraceSummary
from .model.events import EventTiming
from .llm.prompt_builder import build_prompt
from .utils import load_json_config, load_trace_csv


def run_pipeline(
    csv_path,
    frame_count,
    previous_summary=None,
    llm_client=None,
    device_profile="unknown",
):
    df = load_trace_csv(csv_path)
    df = normalize_to_ms(df, frame_count)

    # start logic to apply budgets and highlight violations
    full_budget_config = load_json_config("budgets.json")

    event_budgets = full_budget_config["profiles"][device_profile]["events"]
    fps_target = full_budget_config["profiles"][device_profile]["expected_fps"]

    df = apply_budgets(df, event_budgets)

    violations = df[df["over_budget"]].sort_values("over_budget_ms", ascending=False)

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
    # end logic to apply budgets and highlight violations

    # start logic to generate critical event summary
    critical_events = load_json_config("perf_metadata.json")["performance_metadata"]
    critical_events_df = df[df["Name"].isin(critical_events)]

    critical_events_summary = []
    for _, row in critical_events_df.iterrows():
        critical_events_summary.append(
            EventTiming(
                name=row["Name"],
                frame_time_ms=row["frame_time_ms"],
                budget_ms=row["budget_ms"],
                over_budget_ms=row["over_budget_ms"],
            )
        )
    # end logic to generate critical event summary

    summary = TraceSummary(
        device_profile=device_profile,
        fps_target=fps_target,
        top_violations=top_violations,
        critical_events=critical_events_summary,
        regressions={},
        improvements={},
    )

    if llm_client:
        prompt = build_prompt(summary)
        report = llm_client.generate(prompt)
        return summary, report

    return summary, None
