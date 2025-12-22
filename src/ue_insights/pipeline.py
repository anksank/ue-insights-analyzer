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
    # load the utrace csv file
    df = load_trace_csv(csv_path)

    # normalize the frame times to ms
    df = normalize_to_ms(df, frame_count)

    # fetch the budgets for current device profile
    full_budget_config = load_json_config("budgets.json")

    device_profile = device_profile.lower()
    event_budgets = full_budget_config["profiles"][device_profile]["events"]
    fps_target = full_budget_config["profiles"][device_profile]["expected_fps"]

    # apply the budgets to the dataframe
    df = apply_budgets(df, event_budgets)

    # START_LOGIC to generate critical event summary along with violations
    critical_events = load_json_config("perf_metadata.json")["critical_event_metadata"]
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
    # END_LOGIC to generate critical event summary along with violations

    # START_LOGIC to generate tick event summary
    tick_events = load_json_config("perf_metadata.json")["tick_metrics"]
    tick_events_df = df[df["Name"].isin(tick_events)]

    tick_events_summary = []
    for _, row in tick_events_df.iterrows():
        tick_events_summary.append(
            EventTiming(
                name=row["Name"],
                frame_time_ms=row["frame_time_ms"],
                budget_ms=None,
                over_budget_ms=None,
            )
        )
    # END_LOGIC to generate tick event summary

    summary = TraceSummary(
        device_profile=device_profile,
        fps_target=fps_target,
        critical_events=critical_events_summary,
        tick_events=tick_events_summary,
        regressions={},
        improvements={},
    )

    if llm_client:
        prompt = build_prompt(summary)
        report = llm_client.generate(prompt)
        return summary, report

    return summary, None
