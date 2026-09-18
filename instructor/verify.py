#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Проверка комплекта дня 13. Запускать при поднятом стенде:

    bash stand/run.sh &
    python3 instructor/verify.py

Проверяет две вещи: что все улики в данных сходятся между собой и что
README не ссылается на несуществующие файлы, а файлов без упоминания нет.
Скрипт сам переходит в корень проекта, откуда бы его ни запустили.
"""
import csv, sqlite3, json, hashlib, math, os, re, email, sys
import urllib.request, urllib.error
from datetime import datetime

_HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.dirname(_HERE) if os.path.basename(_HERE) == "instructor" else _HERE)

FAILS = []

def ok(name, got, exp):
    good = got == exp
    if not good:
        FAILS.append(name)
    print(("OK   " if good else "FAIL ") + name + ": " + str(got) +
          ("" if good else "   ожидалось " + str(exp)))

def norm(s):
    for f in ("%Y-%m-%d %H:%M:%S", "%d.%m.%Y %H:%M:%S"):
        try:
            return datetime.strptime(s, f)
        except ValueError:
            pass
    raise ValueError(s)

print("=== Данные ===")
con = sqlite3.connect(":memory:")
con.create_function("norm", 1, lambda s: norm(s).strftime("%Y-%m-%d %H:%M:%S"))
con.execute("CREATE TABLE access (ts,login,ip,action,object,result,auth_method,session_id,detail)")
con.execute("CREATE TABLE geoip (ip,city,lat REAL,lon REAL,org)")
for t, p in (("access", "data/access.csv"), ("geoip", "data/geoip.csv")):
    rows = [tuple(r.values()) for r in csv.DictReader(open(p, encoding="utf-8"))]
    con.executemany("INSERT INTO %s VALUES (%s)" % (t, ",".join("?" * len(rows[0]))), rows)

ok("строк журнала", con.execute("SELECT COUNT(*) FROM access").fetchone()[0], 1042)
ok("различных login", con.execute("SELECT COUNT(DISTINCT login) FROM access").fetchone()[0], 8)
ok("выгрузок", con.execute("SELECT COUNT(*) FROM access WHERE action='export'").fetchone()[0], 2)
ok("формат ISO", con.execute("SELECT COUNT(*) FROM access WHERE ts LIKE '____-%'").fetchone()[0], 893)
ok("12 сент по UTC", con.execute("SELECT COUNT(*) FROM access WHERE norm(ts) LIKE '2026-09-12%'").fetchone()[0], 5)
ok("k.efimov событий", con.execute("SELECT COUNT(*) FROM access WHERE login='k.efimov'").fetchone()[0], 0)
ok("p.kotov в ночь", con.execute("SELECT COUNT(*) FROM access WHERE login='p.kotov' AND norm(ts)>'2026-09-11 15:00:00'").fetchone()[0], 0)
ok("пустых ip", con.execute("SELECT COUNT(*) FROM access WHERE ip=''").fetchone()[0], 0)

def hav(a, b):
    la1, lo1, la2, lo2 = map(math.radians, [a[0], a[1], b[0], b[1]])
    h = math.sin((la2-la1)/2)**2 + math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2 * 6371 * math.asin(math.sqrt(h))

ev = con.execute("SELECT norm(a.ts) t,g.city,g.lat,g.lon,a.session_id FROM access a "
                 "JOIN geoip g ON g.ip=a.ip WHERE a.login='a.sokolov' AND a.action='login' "
                 "AND a.result='ok' ORDER BY t").fetchall()
p, c = ev[-2], ev[-1]
dt = (datetime.fromisoformat(c[0]) - datetime.fromisoformat(p[0])).total_seconds() / 3600
ok("маршрут", p[1] + "->" + c[1], "Сочи->Москва")
ok("скорость км/ч", round(hav((p[2], p[3]), (c[2], c[3])) / dt), 13248)
ok("сессия выгрузки", c[4], "s09981")

ph = [f for f in sorted(os.listdir("data/mail"))
      if "spf=fail" in email.message_from_string(
          open("data/mail/" + f, encoding="utf-8").read()).get("Authentication-Results", "")]
ok("фишинговых писем", ph, ["m03.eml"])

tk = list(csv.DictReader(open("data/tickets.csv", encoding="utf-8")))
res = [t for t in tk if t["action_taken"].startswith("mfa_reset")]
ok("сбросов MFA", len(res), 5)
ok("без подтверждения", [t["id"] for t in res if t["callback_verified"] == "no"], ["T-4471"])

lk = list(csv.DictReader(open("data/leaked_sample.csv", encoding="utf-8")))
ok("строк утечки", len(lk), 10412)
ok("субъектов", len({r["client_id"] for r in lk}), 9380)
arch = {r["client_id"] for r in lk if r["fio"]}
best = [fn for fn in sorted(os.listdir("stand/storage"))
        if len(arch & {r["client_id"] for r in csv.DictReader(
            open("stand/storage/" + fn, encoding="utf-8"))}) == len(arch)]
ok("совпавший бэкап", best, ["clients_2026-06.csv"])

hist = open("data/export_tool/history.log", encoding="utf-8").read()
tok = re.search(r'SERVICE_TOKEN = "([^"]+)"', hist)
ok("токен из репозитория", tok.group(1), "EXP-9f3a7c21b8e4")
ok("коммит", re.findall(r"commit (\w+)", hist[:tok.start()])[-1], "c4d9e1a")

au = [json.loads(l) for l in open("data/audit.jsonl", encoding="utf-8")]
def rh(r):
    raw = "%s|%s|%s|%s|%s|%s" % (r["seq"], r["ts"], r["actor"], r["action"],
                                 json.dumps(r["payload"], sort_keys=True, ensure_ascii=False),
                                 r["prev_hash"])
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()
ok("разрывов цепочки", [r["seq"] for r in au if rh(r) != r["hash"]], [91])
ok("записей журнала", len(au), 126)

print("\n=== Стенд ===")
def code(url, hdr=None):
    try:
        r = urllib.request.urlopen(urllib.request.Request(url, headers=hdr or {}), timeout=5)
        return r.status, len(r.read())
    except urllib.error.HTTPError as e:
        return e.code, 0
    except Exception as e:
        return "нет связи (%s)" % type(e).__name__, 0

base = "http://127.0.0.1:%s" % os.environ.get("PANEL_PORT", "8013")
s1, n1 = code(base + "/backup/clients_2026-06.csv")
if isinstance(s1, str):
    print("   стенд не поднят — раздел пропущен. Запустите: bash stand/run.sh")
else:
    ok("бэкап без авторизации", s1, 200)
    ok("байт совпало с логом", n1, 366887)
    ok("export без сессии", code(base + "/api/export")[0], 401)
    ok("config без токена", code(base + "/api/config")[0], 401)
    ok("config по токену", code(base + "/api/config", {"X-Auth-Token": "EXP-9f3a7c21b8e4"})[0], 200)
    ok("config по чужому токену", code(base + "/api/config", {"X-Auth-Token": "nope"})[0], 403)

print("\n=== Ссылки в README ===")
readme = open("README.md", encoding="utf-8").read()
mentioned = set(re.findall(r"(?<![A-Za-z0-9_/-])((?:data|materials|stand)/[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*)", readme))
missing = sorted(m for m in mentioned if not os.path.exists(m))
ok("упомянутых, но отсутствующих файлов", missing, [])

on_disk = set()
for root, dirs, files in os.walk("."):
    if any(x in root for x in (".git", "instructor", "__pycache__", "storage", "mail")):
        continue
    for f in files:
        rel = os.path.relpath(os.path.join(root, f), ".")
        if rel.split(os.sep)[0] in ("data", "materials", "stand"):
            on_disk.add(rel.replace(os.sep, "/"))
unreferenced = sorted(f for f in on_disk if f not in mentioned)
ok("файлов без упоминания в README", unreferenced, [])
ok("заглушек в README", re.findall(r"\[[А-ЯЁ_]{4,}\]", readme), [])

print()
print("ИТОГ: " + ("все проверки прошли" if not FAILS else "провалено: " + ", ".join(FAILS)))
sys.exit(1 if FAILS else 0)
