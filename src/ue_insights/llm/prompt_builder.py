import json

def build_prompt(summary):
    payload = {
        "device_profile": summary.device_profile,
        "fps_target": summary.fps_target,
        "top_violations": [e.__dict__ for e in summary.top_violations],
        "regressions": summary.regressions,
        "improvements": summary.improvements,
    }

    return f"""
You are a senior Unreal Engine performance engineer.

Tasks:
1. Identify critical frame time issues
2. Explain likely Unreal Engine causes
3. Highlight regressions
4. Suggest next steps

Data:
{json.dumps(payload, indent=2)}
"""
