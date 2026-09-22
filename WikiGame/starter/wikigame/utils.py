from __future__ import annotations

import time
from dataclasses import dataclass


def normalize_title(title: str) -> str:
    return title.strip().replace("_", " ")


@dataclass(frozen=True)
class Timer:
    started_at: float

    @classmethod
    def start(cls) -> "Timer":
        return cls(started_at=time.perf_counter())

    def seconds(self) -> float:
        return time.perf_counter() - self.started_at

