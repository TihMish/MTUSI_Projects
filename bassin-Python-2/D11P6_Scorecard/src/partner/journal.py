"""Ручной журнал исследования. Здесь нет оценки моделью или автотестами."""
import sqlite3

from common import JOURNAL, ROOT, show

DIMENSIONS = ('meaning', 'calculation', 'missing', 'ambiguity', 'stability')
VERDICTS = ('pass', 'fail', 'unclear', 'na')


def line(label):
    while True:
        value = input(label + ': ').strip()
        if value:
            return value
        print('Нужен непустой текст.')


def block(label, required=True):
    while True:
        print(label + '. Заверши отдельной строкой :::END:::')
        rows = []
        while True:
            value = input()
            if value == ':::END:::':
                break
            rows.append(value)
        value = '\n'.join(rows)
        if value.strip() or not required:
            return value
        print('Текст обязателен.')


def choose(label, choices):
    while True:
        value = line(label + ' [' + ', '.join(choices) + ']')
        if value in choices:
            return value
        print('Выбери одно из указанных значений.')


def number(label):
    return int(line(label))


def require_row(con, table, key, value):
    # Имена таблиц передаёт только этот помощник, не пользователь.
    row = con.execute('SELECT * FROM ' + table + ' WHERE ' + key + ' = ?', (value,)).fetchone()
    if row is None:
        raise ValueError('Нет записи с таким номером: ' + table)
    return row


def add_case(con):
    dim = choose('Основной dimension', DIMENSIONS)
    kind = 'pair' if dim == 'stability' else choose('Вид', ('normal', 'challenge'))
    title = line('Короткое название')
    expected = block('Ожидаемое поведение ДО запуска')
    proof = block('Твой SQL для доказательства или пустой ввод', required=False)
    reason = block('Почему это доказательство и какие строки важны')
    cursor = con.execute('INSERT INTO cases(dimension_id,kind,title,expected,proof_sql,proof_reason) VALUES(?,?,?,?,?,?)',
                         (dim, kind, title, expected, proof, reason))
    print('Случай:', cursor.lastrowid)


def add_prompt(con):
    case_id = number('Номер случая')
    require_row(con, 'cases', 'case_id', case_id)
    label = choose('Версия формулировки', ('original', 'paraphrase', 'shortened'))
    text = block('Точный текст вопроса без общего контекста')
    cursor = con.execute('INSERT INTO prompts(case_id,label,text) VALUES(?,?,?)', (case_id, label, text))
    print('Формулировка:', cursor.lastrowid)


def add_attempt(con):
    prompt_id = number('Номер формулировки')
    require_row(con, 'prompts', 'prompt_id', prompt_id)
    model = line('Название модели как показано в интерфейсе')
    conditions = block('Условия запуска: дата, новый чат, настройки, автор, доступность инструментов')
    phase = choose('Этап: свой опыт, обмен, исправление', ('main', 'peer', 'defense'))
    context = (ROOT / 'datasets' / 'model_context.txt').read_text(encoding='utf-8')
    if phase == 'defense':
        context = block('Полный изменённый контекст без самого вопроса')
    response = block('Полный ответ модели БЕЗ правок')
    sql = block('SQL модели без разметки или пустой ввод', required=False)
    result = block('Полный результат запуска SQL либо почему SQL нет или он не запускался')
    cursor = con.execute('INSERT INTO attempts(prompt_id,model,conditions,phase,context_text,response_text,model_sql,execution_result) VALUES(?,?,?,?,?,?,?,?)',
                         (prompt_id, model, conditions, phase, context, response, sql, result))
    print('Попытка:', cursor.lastrowid)


def add_pair(con):
    left = number('Номер первого ответа')
    right = number('Номер второго ответа')
    query = ('SELECT a.attempt_id,a.prompt_id,a.model,a.phase,p.case_id,c.dimension_id '
             'FROM attempts a JOIN prompts p ON p.prompt_id=a.prompt_id '
             'JOIN cases c ON c.case_id=p.case_id WHERE a.attempt_id=?')
    a, b = con.execute(query, (left,)).fetchone(), con.execute(query, (right,)).fetchone()
    if not a or not b:
        raise ValueError('Один из ответов не найден.')
    if a[4] != b[4] or a[5] != 'stability' or b[5] != 'stability':
        raise ValueError('Нужны ответы одного случая с dimension stability.')
    if a[1] == b[1] or a[2:4] != b[2:4]:
        raise ValueError('Нужны разные формулировки, одна модель и один этап.')
    if con.execute('SELECT 1 FROM pairs WHERE left_attempt_id=? AND right_attempt_id=?', (right, left)).fetchone():
        raise ValueError('Эта пара уже записана в обратном порядке.')
    note = block('Почему смысл вопросов одинаков и условия сопоставимы')
    cursor = con.execute('INSERT INTO pairs(left_attempt_id,right_attempt_id,note) VALUES(?,?,?)', (left, right, note))
    print('Пара:', cursor.lastrowid)


def add_assessment(con):
    kind = choose('Оценка ответа или пары', ('attempt', 'pair'))
    item_id = number('Номер ответа или пары')
    if kind == 'attempt':
        require_row(con, 'attempts', 'attempt_id', item_id)
        dim = choose('Dimension', DIMENSIONS[:-1])
        attempt_id, pair_id = item_id, None
    else:
        require_row(con, 'pairs', 'pair_id', item_id)
        dim = 'stability'
        attempt_id, pair_id = None, item_id
    print('pass = прошёл; fail = не прошёл; unclear = спорно; na = не применимо')
    verdict = choose('Твоя ручная оценка', VERDICTS)
    reason = block('Доказательство оценки: строки, расчёт, объяснение')
    author = line('Твой учебный псевдоним')
    cursor = con.execute('INSERT INTO assessments(attempt_id,pair_id,dimension_id,verdict,reason,assessed_by) VALUES(?,?,?,?,?,?)',
                         (attempt_id, pair_id, dim, verdict, reason, author))
    print('Ручная оценка:', cursor.lastrowid)


def add_note(con):
    cursor = con.execute('INSERT INTO notes(topic,text) VALUES(?,?)', (line('Тема'), block('Текст заметки')))
    print('Заметка:', cursor.lastrowid)


def correct_assessment(con):
    item_id = number('Номер ошибочно введённой оценки')
    old = require_row(con, 'assessments', 'assessment_id', item_id)
    verdict = choose('Исправленное значение', VERDICTS)
    reason = block('Новая причина оценки')
    why = block('Почему исправляешь запись')
    author = line('Кто исправляет')
    con.execute('INSERT INTO notes(topic,text) VALUES(?,?)',
                ('Исправление оценки', 'Оценка %d. Старая запись: %r\nНовая оценка: %s\nПричина: %s\nИзменил: %s\nОбъяснение: %s' %
                 (item_id, old, verdict, reason, author, why)))
    con.execute('UPDATE assessments SET verdict=?,reason=?,assessed_by=? WHERE assessment_id=?',
                (verdict, reason, author, item_id))
    print('Исправление записано. Прежнее значение сохранено в заметке.')


def list_records(con):
    tables = ('dimensions', 'cases', 'prompts', 'attempts', 'pairs', 'assessments', 'notes')
    table = choose('Таблица', tables)
    if table == 'attempts':
        sql = 'SELECT attempt_id,prompt_id,model,phase,created_at FROM attempts'
    elif table == 'notes':
        sql = 'SELECT note_id,topic,created_at FROM notes'
    else:
        sql = 'SELECT * FROM ' + table
    show(con.execute(sql))


def main():
    if not JOURNAL.is_file():
        print('Сначала выполни python3 src/partner/prepare.py')
        return
    con = sqlite3.connect(str(JOURNAL))
    con.execute('PRAGMA foreign_keys = ON')
    actions = {'1': add_case, '2': add_prompt, '3': add_attempt,
               '4': add_pair, '5': add_assessment, '6': add_note,
               '7': list_records, '8': correct_assessment}
    print('Журнал ничего не оценивает. Оценки вводишь ты.')
    try:
        while True:
            print('\n1 Случай | 2 Формулировка | 3 Ответ | 4 Пара | 5 Оценка')
            print('6 Заметка | 7 Просмотр | 8 Исправление оценки | 0 Выход')
            choice = input('Выбор: ').strip()
            if choice == '0':
                break
            if choice not in actions:
                print('Нет такого действия.')
                continue
            try:
                with con:
                    actions[choice](con)
            except (ValueError, sqlite3.Error, OSError) as exc:
                print('Запись не сохранена:', exc)
    except (EOFError, KeyboardInterrupt):
        con.rollback()
        print('\nНезавершённая запись отменена. Предыдущие записи сохранены.')
    finally:
        con.close()


if __name__ == '__main__':
    main()
