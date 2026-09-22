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

    queue = deque([(start, 0)])
    visited: set[str] = {start}
    parent: dict[str, Optional[str]] = {start: None}

    visited_pages = 0

    while queue:
        current, depth = queue.popleft()
        visited_pages += 1

        if visited_pages > max_pages:
            return None

        if depth >= max_depth:
            continue

        try:
            links = provider.get_links(current)
        except Exception:
            continue

        for link in links:
            link = normalize_title(link)

            if link in visited:
                continue

            visited.add(link)
            parent[link] = current

            if link == goal:
                path: list[str] = []
                node: Optional[str] = goal
                while node is not None:
                    path.append(node)
                    node = parent[node]
                path.reverse()
                return SearchResult(path=path, visited_pages=visited_pages)

            queue.append((link, depth + 1))

    return None
