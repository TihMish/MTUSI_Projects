from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .models import AsyncLinkProvider
from .utils import normalize_title


@dataclass(frozen=True)
class SearchResult:
    path: list[str]
    visited_pages: int


async def find_path_bfs_async(
    start: str,
    goal: str,
    provider: AsyncLinkProvider,
    *,
    max_depth: int = 5,
    max_pages: int = 500,
) -> Optional[SearchResult]:
    """
    Асинхронная версия BFS (заготовка).

    В рамках текущей версии курса реализация не предоставляется.
    """
    start = normalize_title(start)
    goal = normalize_title(goal)

    raise NotImplementedError("Асинхронный BFS в стартере не реализован.")
