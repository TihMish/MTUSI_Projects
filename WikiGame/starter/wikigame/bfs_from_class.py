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
    """
    Ищет кратчайший путь (минимум кликов) от start до goal по ссылкам Википедии.

    Ограничения:
      - max_depth: не идём глубже N кликов
      - max_pages: не разворачиваем больше N страниц
    """
    start = normalize_title(start)
    goal = normalize_title(goal)

    if start == goal:
        return SearchResult(path=[start], visited_pages=0)

    queue: deque[str] = deque([start])
    parent: dict[str, Optional[str]] = {start: None}
    depth: dict[str, int] = {start: 0}

    visited_pages = 0

    while queue:
        current = queue.popleft()
        cur_depth = depth[current]

        if cur_depth >= max_depth:
            continue

        if visited_pages >= max_pages:
            break

        neighbors = provider.get_links(current)
        visited_pages += 1

        for next_neighbor in neighbors:
            if next_neighbor in parent:
                continue

            parent[next_neighbor] = current
            depth[next_neighbor] = cur_depth + 1

            if next_neighbor == goal:
                path = [goal]
                vertex = goal
                while parent[vertex] is not None:
                    vertex = parent[vertex]
                    path.append(vertex)
                path.reverse()
                return SearchResult(path=path, visited_pages=visited_pages)

            queue.append(next_neighbor)

    return None
