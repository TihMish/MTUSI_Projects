"""Запускает SQL только для чтения. Не оценивает ответы."""
import argparse
import sqlite3
import sys
from pathlib import Path

from common import readonly, show, split_sql


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('database')
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument('--sql')
    source.add_argument('--file')
    source.add_argument('--tables', action='store_true')
    args = parser.parse_args()
    if args.tables:
        sql = "SELECT name, sql FROM sqlite_master WHERE type='table' ORDER BY name"
    elif args.file:
        sql = Path(args.file).read_text(encoding='utf-8')
    else:
        sql = args.sql
    con = readonly(args.database)
    try:
        for statement in split_sql(sql):
            steps = [0]

            def stop_long_query():
                steps[0] += 1
                return 1 if steps[0] > 2000 else 0

            con.set_progress_handler(stop_long_query, 1000)
            show(con.execute(statement))
    finally:
        con.close()
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, sqlite3.Error) as exc:
        print('Запрос не выполнен:', exc, file=sys.stderr)
        print('База открыта только для чтения. Сообщение не является оценкой модели.', file=sys.stderr)
        sys.exit(1)
