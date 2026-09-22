# WikiGame: шаблон для участников

Это репозиторий‑заготовка: сетевые клиенты к `ru.wikipedia.org` уже есть, а алгоритм поиска пути (BFS) нужно реализовать самостоятельно.

## Навигация
- `starter/wikigame/bfs.py` — TODO: синхронный BFS (основное задание).
- `starter/wikigame/bfs_async.py` — TODO: асинхронный BFS (не обязателен/не реализован в стартере).
- `starter/wikigame/wiki_client_sync.py` — готовый sync‑клиент MediaWiki API (с кешем, `plnamespace=0`, `redirects=1`, `continue`).
- `starter/wikigame/wiki_client_async.py` — готовый async‑клиент (aiohttp + лимит конкурентности).
- `starter/wikigame/cli.py` — CLI (`--mode sync/async`).
- `starter/tests/` — офлайн‑тесты для BFS (без интернета).

## Быстрый старт

```bash
cd git/starter
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
pytest -q
```

Тесты будут падать, пока не реализован BFS в `starter/wikigame/bfs.py`.

## Запуск CLI (после реализации BFS)

```bash
cd git/starter
python -m wikigame --start "Питон" --goal "Гвидо ван Россум" --max-depth 4 --max-pages 300
```

## Если падает SSL (`SSLCertVerificationError`)
Правильный вариант — передать свой CA bundle:

```bash
cd git/starter
python -m wikigame --ca-bundle /path/to/ca.pem --start "Питон" --goal "Гвидо ван Россум"
```

Крайний вариант (только для локальной отладки):

```bash
cd git/starter
python -m wikigame --insecure --start "Питон" --goal "Гвидо ван Россум"
```
