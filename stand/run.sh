#!/usr/bin/env bash
# Поднимает учебную копию «Пульта смотрителя» на 127.0.0.1.
# Ничего не устанавливает: нужен только python3 со стандартной библиотекой.
set -e
cd "$(dirname "$0")/.."
PORT="${PANEL_PORT:-8013}"
echo "Стенд поднимается на http://127.0.0.1:${PORT}/"
echo "Остановить — Ctrl+C."
PANEL_PORT="$PORT" exec python3 stand/panel.py
