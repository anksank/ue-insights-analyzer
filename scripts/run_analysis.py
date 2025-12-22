import sys
from pathlib import Path

# Add src to path so we can import ue_insights
script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent
sys.path.append(str(project_root / "src"))

from ue_insights.pipeline import run_pipeline  # noqa: E402
from ue_insights.utils import load_trace_csv  # noqa: E402

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def get_event_count(df, event_name_inner: str) -> int:
    """Fetch the Count value for a given event name from the dataframe."""
    row = df[df["Name"] == event_name_inner]
    if not row.empty:
        return int(row["Count"].values[0])
    else:
        raise ValueError(f"Event '{event_name_inner}' not found in dataframe")


def main(in_trace_file, device_profile):
    # Load CSV
    df = load_trace_csv(in_trace_file)

    # count the number of frames to analyze
    frame_count = get_event_count(df, "FEngineLoop::Tick")

    # Run the pipeline
    # Pass None for llm_client for now as requested
    summary, _ = run_pipeline(
        csv_path=in_trace_file,
        frame_count=frame_count,
        previous_summary=None,
        llm_client=None,
        device_profile=device_profile,
    )

    print("\nPipeline Summary:")
    print(f"Top Violations: {len(summary.top_violations)}")
    for v in summary.top_violations:
        print(
            f" - {v.name}: {v.frame_time_ms:.2f}ms (Budget: {v.budget_ms:.2f}ms, Over: {v.over_budget_ms:.2f}ms)"
        )

    for v in summary.critical_events:
        print(f" - {v.name}: {v.frame_time_ms:.2f}ms")

    # Generate Markdown report for violations
    markdown_report_path = "violations_report.md"
    with open(markdown_report_path, "w", encoding="utf-8") as f:
        f.write("# Performance report for {in_trace_file}\n\n")
        f.write("| Event Name | Frame Time (ms) | Budget (ms) | Over Budget (ms) |\n")
        f.write("| :--- | :---: | :---: | :---: |\n")
        for v in summary.top_violations:
            f.write(
                f"| {v.name} | {v.frame_time_ms:.2f} | {v.budget_ms:.2f} | {v.over_budget_ms:.2f} |\n"
            )

    print(f"Markdown violations report generated: {markdown_report_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: py stats.py <trace_file> <target_FPS -low/mid/high/ultra>")
        sys.exit(1)

    trace_file = sys.argv[1]
    target_fps = sys.argv[2]
    main(trace_file, target_fps)
