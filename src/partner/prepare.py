"""Подготовка журнала, не проверка решения."""
import sqlite3
import sys

from common import JOURNAL, ROOT, STATION, readonly


def main():
    if sys.version_info < (3, 8):
        print('Нужен уже установленный Python 3.8 или новее. Обратись к стаффу.')
        return 1
    print('Python:', sys.version.split()[0])
    print('SQLite:', sqlite3.sqlite_version)
    with readonly(STATION) as con:
        count = con.execute('SELECT COUNT(*) FROM experiments').fetchone()[0]
    print('Учебная база доступна. Опытов:', count)
    if JOURNAL.exists():
        print('src/results.db уже существует. Записи оставлены без изменений.')
        return 0
    with sqlite3.connect(str(JOURNAL)) as con:
        con.executescript((ROOT / 'data' / 'journal_schema.sql').read_text(encoding='utf-8'))
    print('Создан пустой журнал src/results.db. Это не проверка работы.')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, sqlite3.Error) as exc:
        print('Не удалось подготовить файлы:', exc)
        print('Передай сообщение стаффу. Ничего не устанавливай.')
        sys.exit(1)
