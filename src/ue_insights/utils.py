import json
import sys
from pathlib import Path
import pandas as pd

def load_json_config(config_name):
    """Load budget configuration from JSON file."""
    # Config is in the same package, under "config" subdirectory
    # This assumes utils.py is in src/ue_insights/ and config is src/ue_insights/config/
    current_dir = Path(__file__).resolve().parent
    config_path = current_dir / "config" / config_name
    
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Config file not found at {config_path}")
        sys.exit(1)


def load_trace_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, encoding="utf-16")
    # df["Name"] = df["Name"].str.strip()
    return df
