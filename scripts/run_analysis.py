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


def analyze_trace(in_trace_file, device_profile):
    """Analyze a single trace file and return the summary."""
    # Load CSV
    df = load_trace_csv(in_trace_file)

    # count the number of frames to analyze
    frame_count = get_event_count(df, "FEngineLoop::Tick")

    # Run the pipeline
    summary, _ = run_pipeline(
        csv_path=in_trace_file,
        frame_count=frame_count,
        previous_summary=None,
        llm_client=None,
        device_profile=device_profile,
    )

    print(f"\nPipeline Summary for {device_profile}:")
    for v in summary.critical_events:
        print(
            f" - {v.name}: {v.frame_time_ms:.2f}ms (Budget: {v.budget_ms:.2f}ms, Over: {v.over_budget_ms:.2f}ms)"
        )

    return summary


def generate_consolidated_report(summaries, folder_name):
    """Generate a single markdown report for all device profiles.

    Args:
        summaries: dict mapping (device_name, device_profile) tuples to TraceSummary objects
        folder_name: name of the folder for report title
    """
    reports_dir = project_root / "data" / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    markdown_report_path = reports_dir / f"{folder_name}_performance_report.md"

    # Get ordered list of keys and event names
    summary_keys = list(summaries.keys())

    # Get critical event names from first summary (assuming all have same events)
    first_summary = next(iter(summaries.values()))
    critical_event_names = [v.name for v in first_summary.critical_events]
    tick_event_names = [v.name for v in first_summary.tick_events]

    with open(markdown_report_path, "w", encoding="utf-8") as f:
        f.write(f"# Performance Report for {folder_name}\n\n")

        # Helper function to format value with color based on over_budget
        def format_with_color(value, over_budget):
            if over_budget > 0:
                return f'<span style="color:red">{value:.2f}</span>'
            else:
                return f'<span style="color:green">{value:.2f}</span>'

        # Critical Events Table - Frame Time (with color coding)
        f.write("## Critical Events - Frame Time (ms)\n")
        f.write(
            "| Device Profile | Device Name | "
            + " | ".join(critical_event_names)
            + " |\n"
        )
        f.write(
            "| :---: | :--- | "
            + " | ".join([":---:"] * len(critical_event_names))
            + " |\n"
        )
        for device_name, device_profile in summary_keys:
            summary = summaries[(device_name, device_profile)]
            times = {v.name: v.frame_time_ms for v in summary.critical_events}
            over = {v.name: v.over_budget_ms for v in summary.critical_events}
            row = [
                format_with_color(times.get(name, 0), over.get(name, 0))
                for name in critical_event_names
            ]
            f.write(f"| {device_profile} | {device_name} | " + " | ".join(row) + " |\n")
        f.write("\n")

        # Critical Events Table - Over Budget (with color coding)
        f.write("## Critical Events - Over Budget (ms)\n")
        f.write(
            "| Device Profile | Device Name | "
            + " | ".join(critical_event_names)
            + " |\n"
        )
        f.write(
            "| :---: | :--- | "
            + " | ".join([":---:"] * len(critical_event_names))
            + " |\n"
        )
        for device_name, device_profile in summary_keys:
            summary = summaries[(device_name, device_profile)]
            over = {v.name: v.over_budget_ms for v in summary.critical_events}
            row = [
                format_with_color(over.get(name, 0), over.get(name, 0))
                for name in critical_event_names
            ]
            f.write(f"| {device_profile} | {device_name} | " + " | ".join(row) + " |\n")
        f.write("\n")

        # Tick Events Table (no color - no budget for tick events)
        f.write("## Tick Related Events - Frame Time (ms)\n")
        f.write(
            "| Device Profile | Device Name | " + " | ".join(tick_event_names) + " |\n"
        )
        f.write(
            "| :---: | :--- | " + " | ".join([":---:"] * len(tick_event_names)) + " |\n"
        )
        for device_name, device_profile in summary_keys:
            summary = summaries[(device_name, device_profile)]
            times = {v.name: v.frame_time_ms for v in summary.tick_events}
            row = [f"{times.get(name, 0):.2f}" for name in tick_event_names]
            f.write(f"| {device_profile} | {device_name} | " + " | ".join(row) + " |\n")

    print(f"Consolidated performance report generated: {markdown_report_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: py run_analysis.py <folder_path>")
        sys.exit(1)

    folder_path = Path(sys.argv[1])
    folder_name = folder_path.name

    # Collect summaries from all CSV files
    # Filename format: deviceName_deviceProfile.csv (split on last underscore)
    summaries = {}
    for trace_file in folder_path.glob("*.csv"):
        filename_stem = trace_file.stem
        # Split on last underscore to get device_name and device_profile
        last_underscore_idx = filename_stem.rfind("_")
        if last_underscore_idx != -1:
            device_name = filename_stem[:last_underscore_idx]
            device_profile = filename_stem[last_underscore_idx + 1 :]
        else:
            device_name = filename_stem
            device_profile = "unknown"

        summary = analyze_trace(trace_file, device_profile)
        summaries[(device_name, device_profile)] = summary

    # Generate a single consolidated report
    generate_consolidated_report(summaries, folder_name)
