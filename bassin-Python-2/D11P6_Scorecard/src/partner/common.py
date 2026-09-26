"""Общие функции готовых помощников. Только стандартная библиотека."""
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATION = ROOT / 'data' / 'station.db'
JOURNAL = ROOT / 'src' / 'results.db'


def readonly(path):
    path = Path(path).resolve()
    if not path.is_file():
        raise FileNotFoundError('Нет файла базы: ' + str(path))
    con = sqlite3.connect(path.as_uri() + '?mode=ro', uri=True)
    con.execute('PRAGMA query_only = ON')
    allowed = {sqlite3.SQLITE_SELECT, sqlite3.SQLITE_READ,
               sqlite3.SQLITE_FUNCTION, sqlite3.SQLITE_RECURSIVE}

    def authorize(action, arg1, arg2, db_name, trigger):
        if action == sqlite3.SQLITE_FUNCTION and (arg2 or '').lower() == 'load_extension':
            return sqlite3.SQLITE_DENY
        return sqlite3.SQLITE_OK if action in allowed else sqlite3.SQLITE_DENY

    con.set_authorizer(authorize)
    return con


def split_sql(text):
    """Делит обычный SQLite SQL, не разрезая строку по точке с запятой внутри кавычек."""
    buffer = ''
    for char in text:
        buffer += char
        if char == ';' and sqlite3.complete_statement(buffer):
            yield buffer
            buffer = ''
    if buffer.strip():
        yield buffer


def show(cursor, limit=200):
    if cursor.description is None:
        return
    print(' | '.join(column[0] for column in cursor.description))
    rows = cursor.fetchmany(limit + 1)
    for row in rows[:limit]:
        print(' | '.join('NULL' if value is None else str(value) for value in row))
    if len(rows) > limit:
        print('Вывод сокращён до %d строк. Уточни запрос.' % limit)
    else:
        print('Строк: %d' % len(rows))
