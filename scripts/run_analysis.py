import sys
from pathlib import Path

# Add src to path so we can import ue_insights
script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent
sys.path.append(str(project_root / "src"))

from ue_insights.pipeline import run_pipeline  # noqa: E402
from ue_insights.utils import load_trace_csv  # noqa: E402


def get_event_count(df, event_name_inner: str) -> int:
    """Fetch the Count value for a given event name from the dataframe."""
    row = df[df["Name"] == event_name_inner]
    if not row.empty:
        return int(row["Count"].values[0])
    else:
        raise ValueError(f"Event '{event_name_inner}' not found in dataframe")


def analyze_trace(in_trace_file, device_profile, scenario):
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
    for v in summary.critical_events:
        print(
            f" - {v.name}: {v.frame_time_ms:.2f}ms (Budget: {v.budget_ms:.2f}ms, Over: {v.over_budget_ms:.2f}ms)"
        )

    # Generate Markdown for performance report
    input_csv_name = Path(in_trace_file).stem
    reports_dir = project_root / "data" / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    markdown_report_path = reports_dir / f"{input_csv_name}_performance_report.md"
    with open(markdown_report_path, "w", encoding="utf-8") as f:
        f.write(f"# Performance report for {input_csv_name} [{scenario}]\n\n")
        f.write("## Summary of Critical Events\n")
        f.write("| Event Name | Frame Time (ms) | Budget (ms) | Over Budget (ms) |\n")
        f.write("| :--- | :---: | :---: | :---: |\n")
        for v in summary.critical_events:
            f.write(
                f"| {v.name} | {v.frame_time_ms:.2f} | {v.budget_ms:.2f} | {v.over_budget_ms:.2f} |\n"
            )
        f.write("\n")
        f.write("## Summary of Tick Related Events\n")
        f.write("| Event Name | Frame Time (ms) |\n")
        f.write("| :--- | :---: |\n")
        for v in summary.tick_events:
            f.write(f"| {v.name} | {v.frame_time_ms:.2f} |\n")

    print(f"Performance report generated: {markdown_report_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "Usage: py run_analysis.py <trace_file (yyyymmdd_deviceprofile_scenario.csv)>"
        )
        sys.exit(1)

    folder_path = sys.argv[1]
    # Parse filename: yyyymmdd_deviceprofile_scenario.csv
    for trace_file in Path(folder_path).glob("*.csv"):
        filename_stem = Path(trace_file).stem
        parts = filename_stem.split("_")
        device_profile = parts[0]
        scenario = "_".join(parts[1:]) if len(parts) > 1 else ""
        analyze_trace(trace_file, device_profile, scenario)
