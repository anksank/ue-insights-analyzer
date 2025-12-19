from dataclasses import dataclass

@dataclass
class EventTiming:
    name: str
    frame_time_ms: float
    budget_ms: float | None
    over_budget_ms: float | None
