from __future__ import annotations

import argparse
import asyncio
import sys

from .bfs import SearchResult as SearchResultSync
from .bfs import find_path_bfs
from .bfs_async import SearchResult as SearchResultAsync
from .bfs_async import find_path_bfs_async
from .utils import Timer
from .wiki_client_async import WikiClientAsync
from .wiki_client_sync import WikiClientSync


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="wikigame", description="WikiGame path finder (ru.wikipedia.org)")
    p.add_argument("--start", required=True, help="Стартовая статья (заголовок)")
    p.add_argument("--goal", required=True, help="Целевая статья (заголовок)")
    p.add_argument("--mode", choices=("sync", "async"), default="sync")
    p.add_argument("--max-depth", type=int, default=5)
    p.add_argument("--max-pages", type=int, default=500)
    p.add_argument("--concurrency", type=int, default=10, help="Только для --mode async")
    p.add_argument("--rps-delay", type=float, default=0.0, help="Только для --mode async")
    p.add_argument("--ca-bundle", default=None, help="Путь к CA bundle (.pem) для TLS (если прокси подменяет сертификаты)")
    p.add_argument(
        "--insecure",
        action="store_true",
        help="Отключить проверку TLS сертификата (не рекомендуется; только для локальной отладки)",
    )
    return p


def _print_result(result: SearchResultSync | SearchResultAsync | None, seconds: float) -> int:
    if result is None:
        print(f"Путь не найден. (time={seconds:.2f}s)")
        return 2

    print("Путь найден:")
    print(" -> ".join(result.path))
    print(f"Кликов: {len(result.path) - 1}")
    print(f"Развёрнуто страниц: {result.visited_pages}")
    print(f"Время: {seconds:.2f}s")
    return 0


async def _run_async(args: argparse.Namespace) -> int:
    t = Timer.start()
    if args.insecure:
        print("WARNING: --insecure отключает проверку TLS сертификата.", file=sys.stderr)

    async with WikiClientAsync(
        concurrency=args.concurrency,
        rps_delay=args.rps_delay,
        verify_ssl=not args.insecure,
        ca_bundle=args.ca_bundle,
    ) as client:
        try:
            result = await find_path_bfs_async(
                args.start,
                args.goal,
                client,
                max_depth=args.max_depth,
                max_pages=args.max_pages,
            )
        except NotImplementedError as e:
            print(str(e))
            return 3
    return _print_result(result, t.seconds())


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)

    if args.mode == "async":
        return asyncio.run(_run_async(args))

    t = Timer.start()
    if args.insecure:
        print("WARNING: --insecure отключает проверку TLS сертификата.", file=sys.stderr)

    client = WikiClientSync(verify_ssl=not args.insecure, ca_bundle=args.ca_bundle)
    try:
        result = find_path_bfs(
            args.start,
            args.goal,
            client,
            max_depth=args.max_depth,
            max_pages=args.max_pages,
        )
    except NotImplementedError as e:
        print(str(e))
        return 3
    return _print_result(result, t.seconds())
