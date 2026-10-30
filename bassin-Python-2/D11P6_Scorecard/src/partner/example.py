"""Маленький пример чтения SQLite из Python. Не итоговый отчёт."""
from common import JOURNAL, readonly


def main():
    con = readonly(JOURNAL)
    try:
        sql = 'SELECT dimension_id, title FROM dimensions ORDER BY dimension_id'
        for dimension_id, title in con.execute(sql):
            print(dimension_id + ': ' + title)
    finally:
        con.close()


if __name__ == '__main__':
    main()
