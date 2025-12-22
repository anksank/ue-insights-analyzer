# ue-insights-analyzer
Tool to generate analytical reports from Unreal Insights CSVs powered by LLM models to improve performance

## Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/anksank/ue-insights-analyzer.git
cd ue-insights-analyzer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

Or install as a package:
```bash
pip install -e .
```

## Input Folder Setup

The input folder should be organized as follows:

```
data/input_csv/
└── <session_folder>/          # e.g., 20251122_Automation
    ├── <deviceName>_<deviceProfile>.csv
    ├── <deviceName>_<deviceProfile>.csv
    └── ...
```

### Naming Convention

**Folder name**: Use a descriptive name for the analysis session (e.g., `20251122_Automation`, `Release_Build_Tests`)

**CSV files**: Follow the format `<deviceName>_<deviceProfile>.csv`
- `deviceName` - Name of the device (can contain underscores/spaces), e.g., `Samsung Galaxy S23`, `iPhone_15_Pro`
- `deviceProfile` - Performance profile tier, must match a key in `budgets.json` (e.g., `low`, `mid`, `high`, `ultra`)

**Examples:**
- `testdevice_mid.csv`
- `Samsung Galaxy S23_high.csv`
- `iPhone_15_Pro_Max_ultra.csv`

> **Note**: The device profile is parsed from the **last underscore** in the filename.

## Usage
```bash
python run_analysis.py <folder_path>
```

**Example:**
```bash
python scripts/run_analysis.py data/input_csv/20251122_Automation
```

## Output
The script generates a consolidated markdown report at:
```
data/reports/<folder_name>_performance_report.md
```

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
