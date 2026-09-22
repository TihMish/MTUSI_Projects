from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Optional

from .models import LinkProvider
from .utils import normalize_title


@dataclass(frozen=True)
class SearchResult:
    path: list[str]
    visited_pages: int


def find_path_bfs(
    start: str,
    goal: str,
    provider: LinkProvider,
    *,
    max_depth: int = 5,
    max_pages: int = 500,
) -> Optional[SearchResult]:

    # Двунаправленный поиск в ширину

    start = normalize_title(start)
    goal = normalize_title(goal)

    if start == goal:
        return SearchResult(path=[start], visited_pages=0)

    q_start = deque([start])
    q_goal = deque([goal])

    visited_start: set[str] = {start}
    visited_goal: set[str] = {goal}

    parent_start: dict[str, Optional[str]] = {start: None}
    parent_goal: dict[str, Optional[str]] = {goal: None}

    visited_pages = 0
    depth = 0

    while q_start and q_goal and depth < max_depth:
        depth += 1

        meeting = _expand_layer(
            q_start,
            visited_start,
            visited_goal,
            parent_start,
            provider,
        )
        visited_pages += 1

        if visited_pages > max_pages:
            return None

        if meeting:
            path = _build_path(meeting, parent_start, parent_goal)
            return SearchResult(path=path, visited_pages=visited_pages)

        meeting = _expand_layer(
            q_goal,
            visited_goal,
            visited_start,
            parent_goal,
            provider,
        )
        visited_pages += 1

        if visited_pages > max_pages:
            return None

        if meeting:
            path = _build_path(meeting, parent_start, parent_goal)
            return SearchResult(path=path, visited_pages=visited_pages)

    return None


def _expand_layer(
    queue: deque[str],
    visited_this: set[str],
    visited_other: set[str],
    parent: dict[str, Optional[str]],
    provider: LinkProvider,
) -> Optional[str]:

    # проверка пересечение

    for _ in range(len(queue)):
        current = queue.popleft()

        try:
            links = provider.get_links(current)
        except Exception:
            continue

        for link in links:
            link = normalize_title(link)

            if link in visited_this:
                continue

            visited_this.add(link)
            parent[link] = current

            if link in visited_other:
                return link

            queue.append(link)

    return None


def _build_path(
    meeting: str,
    parent_start: dict[str, Optional[str]],
    parent_goal: dict[str, Optional[str]],
) -> list[str]:

# Восстанавление пути

    path_start: list[str] = []
    node: Optional[str] = meeting
    while node is not None:
        path_start.append(node)
        node = parent_start[node]

    path_goal: list[str] = []
    node = parent_goal.get(meeting)
    while node is not None:
        path_goal.append(node)
        node = parent_goal[node]

    return path_start[::-1] + path_goal
