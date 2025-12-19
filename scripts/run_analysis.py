import sys
import pandas as pd
import json
from pathlib import Path

# Add src to path so we can import ue_insights
script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent
sys.path.append(str(project_root / "src"))

from ue_insights.pipeline import run_pipeline


event_metadata = {
    "base": {
        "FEngineLoop::Tick": {
            "Frame": {
                "FrameTime": {
                    "GameEngine Tick": {
                        "UWorld_Tick": {
                            "World Tick Time": {
                                "Tick Time": {
                                    "TG_PrePhysics": {},
                                    "Start TG_DuringPhysics": {},
                                    "TG_PostPhysics": {},
                                    "TG_StartPhysics": {},
                                    "TG_EndPhysics": {},
                                    "Niagara Manager Tick [GT]": {},
                                    "TG_PostUpdateWork": {},
                                    "TG_LastDemotable": {}
                                },
                                "Net Tick Time": {},
                                "bDoingActorTicks": {},
                                "GT Tickable Time": {}
                            }
                        }
                    },
                    "Slate::Tick (Time and Widgets)": {
                        "Total Slate Tick Time": {
                            "Slate::DrawWindows": {},
                            "PreTickEvent": {},
                            "Slate::TickPlatform": {},
                            "Flush End of Frame Animations": {}
                        }
                    },
                    "Frame Sync Time": {}
                }
            }
        },
        "BeginFrame": {
            "FDrawSceneCommand": {
                "RenderViewFamily": {
                    "STAT_FMobileSceneRenderer_Render": {
                        "InitViews": {},
                        "FinishRenderViewTarget": {},
                        "STAT_ComputeLightGrid": {},
                        "ShaderPrint::BeginView": {},
                        "DeferredShadingSceneRenderer ViewExtensionPostRenderView": {}
                    },
                    "EndFlushResourcesRHI": {},
                    "Scene::UpdateAllPrimitiveSceneInfos": {},
                    "FRDGBuilder::ExecutePasses": {},
                    "Collect Resources": {},
                    "FRDGBuilder::SubmitBufferUploads": {},
                    "FRDGBuilder::CreateUniformBuffers": {},
                    "BeginFlushResourcesRHI": {},
                    "Compile": {}
                },
                "STAT_RenderViewFamily_RenderThread_RHIGetGPUFrameCycles": {},
                "FRDGAllocator::ReleaseAll": {}
            },
            "SlateDrawWindowsCommand": {},
            "SkelMeshObjectUpdateDataCommand": {},
            "DrawWidgetRendererImmediate": {},
            "UpdateTransformCommand": {},
            "HeartbeatTickTickables": {},
            "EndFrame": {},
            "ResetDeferredUpdates": {},
            "BeginRenderingDebugCanvas": {},
            "SetMIParameterValue": {},
            "NiagaraSetDynamicData": {},
            "TickRenderingTimer": {},
            "RenderingFrame": {},
            "FRemovePrimitiveCommand": {}
        },
        "RHI Thread Execute": {
            "SceneEnd": {},
            "Opaque": {},
            "Post": {},
            "After Occlusion Readback": {},
            "Occlusion": {},
            "Translucency": {},
            "SceneStart": {},
            "Shadows": {},
            "SceneSimulation": {},
            "InitViews": {
                "View Visibility": {
                    "ProcessVisibilityTasks": {
                        "WaitUntilTasksComplete": {
                            "ExecuteTask": {
                                "FTickFunctionTask": {},
                                "FParallelAnimationCompletionTask": {},
                                "FNiagaraSystemInstanceFinalizeTask": {},
                                "FSimpleDelegateGraphTask.FinishPhysicsSim": {}
                            }
                        },
                        "ParallelFor": {},
                        "OcclusionCull": {},
                        "BeginInitVisibility 0": {},
                        "FinalizeRelevance": {},
                        "GatherDynamicMeshElements": {},
                        "OcclusionSubmittedFence Wait": {},
                        "MergeSecondaryViewVisibility": {},
                        "Update Fading": {}
                    }
                },
                "FinishVisibility": {},
                "STAT_UpdateIndirectLightingCacheBuffer": {},
                "ParallelMdcDispatchPassSetup": {},
                "FinishDynamicMeshElements": {},
                "FLandscapeSceneViewExtension::PreInitViews_RenderThread": {},
                "GPU Dispatch Setup [RT]": {},
                "STAT_SetupCommonViewUniformBufferParameters": {},
                "Uniform commit time": {},
                "STAT_PostVisibilityFrameSetup": {},
                "FInstanceCullingManager::BeginDeferredCulling": {},
                "Constant buffer update time": {}
            },
            "FXPreRender_Finalize": {},
            "FXPreRender_Prepare": {},
            "FXPreRender_Simulate": {},
            "PrePass": {},
            "AfterInitViews": {},
            "Occlusion Readback": {}
        }
    }
}


def load_budget_config():
    """Load budget configuration from JSON file."""
    # Assuming script is run from project_root/scripts/
    # Config is in project_root/src/ue_insights/config/budgets.json
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent
    config_path = project_root / "src" / "ue_insights" / "config" / "budgets.json"
    
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Config file not found at {config_path}")
        sys.exit(1)

critical_event_budget = load_budget_config()

performance_metadata = [
    "FEngineLoop::Tick",
    "BeginFrame",
    "GameEngine Tick",
    "Slate::Tick (Time and Widgets)",
    "Frame Sync Time",
    "STAT_FEngineLoop_UpdateTimeAndHandleMaxTickRate"
]

critical_event_metadata = [
    "Tick Time",
    "Slate::Tick (Time and Widgets)",
    "Frame Sync Time",
    "RedrawViewports",
    "STAT_FEngineLoop_Tick_SlateInput",
    "Net Tick Time"
]

tick_metrics = [
    "Char Movement Total",
    "USkinnedMeshComponent_TickComponent",
    "AnimGameThreadTime",
    "PlayerController Tick",
    "FStartPhysicsTickFunction_ExecuteTick",
    "Game TaskGraph Stalls"
]

game_thread_metadata = [
    "STAT_FEngineLoop_UpdateTimeAndHandleMaxTickRate",
    "STAT_FEngineLoop_TickFPSChart",
    "FStats::AdvanceFrame",
    "STAT_FEngineLoop_Tick_SlateInput",
    "ProcessAsyncLoading",
    "Net Tick Time",
    "Queue Ticks",
    "Tick Time",
    "GT Tickable Time",
    "Update Camera Time",
    "UpdateStreamingState Time",
    "Tick Time",
    "bDoingActorTicks",
    "NetBroadcastTickTime",
    "TickableGameObjects Time",
    "STAT_Media_TickRender",
    "GameViewport Tick",
    "RedrawViewports",
    "STAT_UGameEngine_Tick_IStreamingManager",
    "STAT_FEngineLoop_ProcessPlayerControllersSlateOperations",
    "Slate::Tick (Platform and Input)",
    "Slate::Tick (Time and Widgets)",
    "Frame Sync Time",
    "Deferred Tick Time"
]

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

DELIMITER = " ==> "


def get_event_list(event_level):
    """Fetch child event names for a given event path from event_metadata."""
    parts = event_level.split(DELIMITER)

    event_list = []
    metadata = event_metadata
    for event_name in parts:
        event_list = metadata.get(event_name, {}).keys()
        metadata = metadata.get(event_name, {})

    return list(event_list)


def get_event_count(df, event_name_inner: str) -> int:
    """Fetch the Count value for a given event name from the dataframe."""
    row = df[df["Name"] == event_name_inner]
    if not row.empty:
        return int(row["Count"].values[0])
    else:
        raise ValueError(f"Event '{event_name_inner}' not found in dataframe")


def analyse_trace(trace_df, frame_count, event_list, b_show_total_time):
    trace_df = trace_df[trace_df["Name"].isin(event_list)].copy()  # <-- make a copy

    trace_df["frame_time"] = (trace_df["Incl"] * 1000) / frame_count

    columns_to_show = ["Name", "frame_time"]
    # Print the dataframe
    print(trace_df[columns_to_show].to_string(index=False))

    if b_show_total_time:
        total_frame_time = trace_df["frame_time"].sum()
        print(f"\nTotal frame_time: {total_frame_time}")

    if "FEngineLoop::Tick" in event_list:
        frame_time = trace_df.loc[trace_df["Name"] == "FEngineLoop::Tick", "frame_time"].values[0]
        print(f"avg. FPS: {1000 / frame_time:2f}")

    return trace_df[columns_to_show]


def analyse_trace_with_budget(trace_df, frame_count, event_list, b_show_total_time, fps_segment):
    trace_df = trace_df[trace_df["Name"].isin(event_list)].copy()  # <-- make a copy

    def get_budget(name):
        return critical_event_budget["profiles"][fps_segment]["events"].get(name, None)

    trace_df["frame_time"] = (trace_df["Incl"] * 1000) / frame_count
    trace_df["budget"] = trace_df["Name"].apply(get_budget)
    trace_df["exceeded_budget"] = trace_df["frame_time"] - trace_df["budget"]
    # trace_df["exceeded_budget_perc"] = (trace_df["exceeded_budget"] / trace_df["budget"]) * 100

    columns_to_show = ["Name", "frame_time", "budget", "exceeded_budget"]
    # Print the dataframe
    print(trace_df[columns_to_show].to_string(index=False))

    if b_show_total_time:
        total_frame_time = trace_df["frame_time"].sum()
        print(f"\nTotal frame_time: {total_frame_time}\n\n")

    if "FEngineLoop::Tick" in event_list:
        frame_time = trace_df.loc[trace_df["Name"] == "FEngineLoop::Tick", "frame_time"].values[0]
        print(f"avg. FPS: {1000 / frame_time:2f}")

    return trace_df[columns_to_show]


def generate_html_report(tables, output_file):
    """
    Generates an HTML report from a list of (title, dataframe) tuples.
    """
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>UTrace Stats Report</title>
        <style>
            body { font-family: sans-serif; margin: 20px; }
            h1 { color: #333; }
            h2 { color: #555; border-bottom: 1px solid #ccc; padding-bottom: 5px; margin-top: 30px; }
            table { border-collapse: collapse; width: 100%; margin-bottom: 20px; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
            tr:nth-child(even) { background-color: #f9f9f9; }
            tr:hover { background-color: #f1f1f1; }
            .negative { color: red; }
            .positive { color: green; }
        </style>
    </head>
    <body>
        <h1>UTrace Stats Report</h1>
    """

    for title, df in tables:
        html_content += f"<h2>{title}</h2>"
        # Convert DataFrame to HTML, avoiding index if possible
        html_table = df.to_html(index=False, classes="table table-striped", float_format="%.2f")
        html_content += html_table

    html_content += """
    </body>
    </html>
    """

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"HTML report generated: {output_file}")


def main(in_trace_file, in_target_fps):
    # Load CSV
    df = pd.read_csv(in_trace_file, encoding="utf-16")

    frame_count = get_event_count(df, "FEngineLoop::Tick")
    budgets = critical_event_budget["profiles"][in_target_fps]["events"]
    
    # Run the pipeline
    # Pass None for llm_client for now as requested
    summary, _ = run_pipeline(
        csv_path=in_trace_file,
        frame_count=frame_count,
        budgets=budgets,
        previous_summary=None,
        llm_client=None,
        device_profile=in_target_fps,
        fps_target=critical_event_budget["profiles"][in_target_fps]["expected_fps"],
    )
    
    print("\n\nPipeline Summary:")
    print(f"Top Violations: {len(summary.top_violations)}")
    for v in summary.top_violations:
        print(f" - {v.name}: {v.frame_time_ms:.2f}ms (Budget: {v.budget_ms:.2f}ms, Over: {v.over_budget_ms:.2f}ms)")


    # report_tables = []

    # print("Analysing Frame Times for performance")
    # df_perf = analyse_trace(df, frame_count, performance_metadata, False)
    # report_tables.append(("Frame Times for Performance", df_perf))

    # print("Analysing Critical Event Metrics")
    # df_crit = analyse_trace_with_budget(df, frame_count, critical_event_metadata, True, in_target_fps)
    # report_tables.append(("Critical Event Metrics", df_crit))

    # print("Analysing Tick Time Metrics")
    # df_tick = analyse_trace(df, frame_count, tick_metrics, True)
    # report_tables.append(("Tick Time Metrics", df_tick))

    # print("Game-thread Events for analysis")
    # df_gt = analyse_trace(df, frame_count, game_thread_metadata, True)
    # report_tables.append(("Game-thread Events", df_gt))

    # # Generate HTML Report
    # output_html = "stats_report.html"
    # generate_html_report(report_tables, output_html)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: py stats.py <trace_file> <target_FPS -low/mid/high/ultra>")
        sys.exit(1)

    trace_file = sys.argv[1]
    target_fps = sys.argv[2]
    main(trace_file, target_fps)