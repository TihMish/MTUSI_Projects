# WikiGame (starter)

Это шаблон проекта для участников: клиенты к `ru.wikipedia.org` готовы, алгоритм BFS — ваш.

## Быстрый старт

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

Тесты будут падать, пока не реализован BFS в `wikigame/bfs.py`.

## Как устроено (коротко)
- `wikigame/bfs.py` — TODO: синхронный BFS (основное задание).
- `wikigame/wiki_client_sync.py` — готовый sync‑клиент MediaWiki API (только ru.wikipedia.org).
- `wikigame/wiki_client_async.py` — готовый async‑клиент (aiohttp + лимиты).
- `wikigame/cli.py` — запуск из командной строки.
- `tests/` — офлайн‑тесты для BFS (без интернета).

## Запуск CLI (русская Википедия)

```bash
python -m wikigame --start "Питон" --goal "Гвидо ван Россум" --max-depth 4 --max-pages 300
```

Async‑режим — заготовка под занятие про `asyncio` (асинхронный BFS в стартере не реализован):

```bash
python -m wikigame --mode async --start "Питон" --goal "Гвидо ван Россум" --max-depth 4 --max-pages 300 --concurrency 10
```

## Если падает SSL (`SSLCertVerificationError`)
Правильный вариант — передать CA bundle: `--ca-bundle /path/to/ca.pem`, крайний — `--insecure` (не рекомендуется).
