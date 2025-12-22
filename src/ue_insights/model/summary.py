from dataclasses import dataclass
from typing import List, Dict
from .events import EventTiming


@dataclass
class TraceSummary:
    device_profile: str
    fps_target: int
    critical_events: list[EventTiming]
    tick_events: list[EventTiming]
    regressions: dict[str, float]
    improvements: dict[str, float]
