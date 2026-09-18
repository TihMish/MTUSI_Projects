#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""«Пульт смотрителя» — учебная копия внутренней панели «Привала».

Один файл, только стандартная библиотека и sqlite3. Слушает 127.0.0.1.
Ничего наружу не отдаёт и никуда не ходит.

Запуск:  bash stand/run.sh      (из корня проекта)
"""
import csv, html, json, os, sqlite3, sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

HERE = os.path.dirname(os.path.abspath(__file__))
STORAGE = os.path.join(HERE, "storage")
PORT = int(os.environ.get("PANEL_PORT", "8013"))

# Конфигурация панели в том виде, в каком её отдаёт /api/config.
CONFIG = {
    "instance": "panel.privalshop.ru (учебная копия)",
    "backup_path": "/backup/",
    "export_endpoint": "/api/export",
    "accounts": ["a.sokolov", "d.kravets", "p.kotov", "m.zueva", "i.bortnik", "s.raifa"],
    "auth_required_paths": ["/api/export", "/api/config"],
    "note": "путь /backup/ исключён из auth_required 2026-08-05 по заявке администратора",
}

# Сервисный токен, который панель считает действующим.
VALID_TOKENS = {"EXP-9f3a7c21b8e4": {"owner": "export_tool", "scope": ["config"]}}

# Учётные записи панели для интерактивного входа.
USERS = {"a.sokolov": "privalspring26", "m.zueva": "zuevaM2026!"}


def load_clients():
    con = sqlite3.connect(":memory:")
    con.execute("CREATE TABLE clients (client_id TEXT, fio TEXT, phone TEXT,"
                " email TEXT, city TEXT, created_at TEXT)")
    path = os.path.join(STORAGE, "clients_2026-06.csv")
    with open(path, encoding="utf-8") as f:
        con.executemany("INSERT INTO clients VALUES (?,?,?,?,?,?)",
                        [tuple(r.values()) for r in csv.DictReader(f)])
    con.commit()
    return con


DB = load_clients()

PAGE = """<!doctype html><html lang="ru"><meta charset="utf-8">
<title>Пульт смотрителя</title>
<style>body{{font:15px/1.5 system-ui,sans-serif;max-width:560px;margin:60px auto;padding:0 16px}}
h1{{font-size:20px}} code{{background:#f2f2f2;padding:1px 5px;border-radius:3px}}
.b{{border:1px solid #ddd;border-radius:8px;padding:14px 16px;margin:14px 0}}</style>
<h1>Пульт смотрителя · учебная копия</h1>
<div class="b"><form method="post" action="/login">
<p><input name="login" placeholder="логин" style="width:180px"></p>
<p><input name="password" type="password" placeholder="пароль" style="width:180px"></p>
<p><button>Войти</button></p></form></div>
<div class="b"><p>Служебные точки входа:</p>
<p><code>/api/config</code> · <code>/api/export</code> · <code>/backup/</code></p></div>
<p style="color:#888">{note}</p>
</html>"""


class Handler(BaseHTTPRequestHandler):
    server_version = "watchman-panel/1.4"

    def log_message(self, fmt, *args):
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def _send(self, code, body, ctype="text/plain; charset=utf-8", extra=None):
        data = body.encode("utf-8") if isinstance(body, str) else body
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(data)

    def _json(self, code, obj):
        self._send(code, json.dumps(obj, ensure_ascii=False, indent=2) + "\n",
                   "application/json; charset=utf-8")

    def do_POST(self):
        if urlparse(self.path).path == "/login":
            n = int(self.headers.get("Content-Length") or 0)
            form = parse_qs(self.rfile.read(n).decode("utf-8"))
            lg = (form.get("login") or [""])[0]
            pw = (form.get("password") or [""])[0]
            if USERS.get(lg) == pw:
                return self._json(200, {"ok": True, "login": lg,
                                        "session": "demo-session", "mfa": "passed"})
            return self._json(401, {"error": "invalid credentials"})
        return self._send(404, "not found\n")

    def do_GET(self):
        p = urlparse(self.path).path

        if p == "/":
            return self._send(200, PAGE.format(note=html.escape(CONFIG["note"])),
                              "text/html; charset=utf-8")

        # /backup/ — авторизация с этого пути снята 2026-08-05
        if p == "/backup/" or p == "/backup":
            names = sorted(os.listdir(STORAGE))
            body = "<!doctype html><meta charset='utf-8'><h2>Index of /backup/</h2><ul>" + \
                   "".join(f"<li><a href='/backup/{html.escape(n)}'>{html.escape(n)}</a></li>"
                           for n in names) + "</ul>"
            return self._send(200, body, "text/html; charset=utf-8")

        if p.startswith("/backup/"):
            name = os.path.basename(p)
            full = os.path.join(STORAGE, name)
            if not os.path.isfile(full):
                return self._send(404, "not found\n")
            with open(full, "rb") as f:
                return self._send(200, f.read(), "text/csv; charset=utf-8",
                                  {"X-Auth-Required": "no"})

        # /api/config — нужен сервисный токен
        if p == "/api/config":
            tok = self.headers.get("X-Auth-Token")
            if not tok:
                return self._json(401, {"error": "auth required",
                                        "hint": "заголовок X-Auth-Token"})
            if tok not in VALID_TOKENS:
                return self._json(403, {"error": "unknown token"})
            return self._json(200, CONFIG)

        # /api/export — нужна сессия интерактивного входа
        if p == "/api/export":
            if self.headers.get("X-Session") != "demo-session":
                return self._json(401, {"error": "auth required",
                                        "hint": "сначала /login, затем заголовок X-Session"})
            q = parse_qs(urlparse(self.path).query)
            limit = int((q.get("limit") or ["20"])[0])
            cur = DB.execute("SELECT client_id, fio, phone, email, city, created_at"
                             " FROM clients LIMIT ?", (limit,))
            buf = ["client_id,fio,phone,email,city,created_at"]
            buf += [",".join(str(x) for x in r) for r in cur]
            return self._send(200, "\n".join(buf) + "\n", "text/csv; charset=utf-8")

        return self._send(404, "not found\n")


if __name__ == "__main__":
    srv = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print(f"Пульт смотрителя слушает http://127.0.0.1:{PORT}/  (Ctrl+C — остановить)")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nостановлен")
