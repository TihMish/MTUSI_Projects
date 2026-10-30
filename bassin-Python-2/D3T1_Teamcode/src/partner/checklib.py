"""Открытая библиотека проверяющего. Решение участника её не импортирует."""
import collections
import hashlib
import json
from pathlib import Path

TOPICS = ('ввод', 'данные', 'ошибки', 'структура')
TYPES = ('one', 'many', 'short', 'output')
LABELS = ('А', 'Б', 'В', 'Г', 'Д')
GROUPS = ('reference', 'review', 'team')

def lines(path):
    if not path.exists():
        return []
    return [s.strip() for s in path.read_text(encoding='utf-8').splitlines()
            if s.strip() and not s.lstrip().startswith('#')]

def raw(path):
    path = Path(path)
    qs, answers = [], collections.defaultdict(list)
    for group in GROUPS:
        for line in lines(path / ('bank_' + group + '.txt')):
            parts = [x.strip() for x in line.split('|')]
            try:
                ident = int(parts[0])
            except (ValueError, IndexError):
                ident = None
            qs.append((group, ident, parts, line))
        for line in lines(path / ('answers_' + group + '.txt')):
            parts = [x.strip() for x in line.split('|')]
            try:
                ident = int(parts[0])
            except (ValueError, IndexError):
                ident = None
            answers[ident].append((group, parts, line))
    return qs, answers

def load(path):
    path = Path(path)
    rows, answers = raw(path)
    counts = collections.Counter(row[1] for row in rows)
    good, errors = [], []
    for group, ident, p, line in rows:
        try:
            assert ident is not None and ident > 0 and counts[ident] == 1
            assert len(p) == 6
            _, topic, level, kind, scale, text = p
            assert topic in TOPICS and kind in TYPES and scale in ('0', '1') and text
            assert (scale == '0' and level == '') or (scale == '1' and level in '12345' and len(level) == 1)
            opts = []
            for agroup, ap, _ in answers.get(ident, []):
                assert agroup == group and len(ap) == 4 and ap[2] in ('0', '1') and ap[3]
                opts.append({'label': ap[1], 'correct': ap[2] == '1', 'text': ap[3]})
            code, expected = '', ''
            if kind in ('one', 'many'):
                assert 2 <= len(opts) <= 5
                labels = [o['label'] for o in opts]
                assert len(set(labels)) == len(labels) and all(x in LABELS for x in labels)
                correct = sum(o['correct'] for o in opts)
                assert correct == 1 if kind == 'one' else 2 <= correct <= len(opts)
            elif kind == 'short':
                assert opts and all(o['label'] == '-' and o['correct'] for o in opts)
            else:
                assert not opts
                code = (path / 'snippets' / f'{ident}.py').read_text(encoding='utf-8')
                expected = (path / 'snippets' / f'{ident}.out').read_text(encoding='utf-8')
                assert code.strip() and len(expected.splitlines()) == 1 and expected.strip()
            good.append({'id': ident, 'topic': topic, 'level': int(level) if level else None,
                         'type': kind, 'scale': int(scale), 'text': text, 'options': opts,
                         'code': code, 'expected': expected})
        except (AssertionError, OSError, UnicodeError, ValueError):
            errors.append({'id': ident, 'line': line})
    return {'questions': good, 'total': len(rows), 'broken': len(errors), 'errors': errors}

def check(q, answer):
    if answer is None or not answer.strip():
        return 'не принят'
    value = answer.strip()
    if q['type'] in ('one', 'many'):
        labels = {o['label'] for o in q['options']}
        tokens = value.upper().split()
        if not tokens or any(t not in labels for t in tokens):
            return 'не принят'
        if q['type'] == 'one' and len(tokens) != 1:
            return 'не принят'
        valid = set(tokens) == {o['label'] for o in q['options'] if o['correct']}
    elif q['type'] == 'short':
        valid = value.lower() in {o['text'].strip().lower() for o in q['options']}
    else:
        valid = value == q['expected'].strip()
    return 'верно' if valid else 'неверно'

def presentation(q):
    content = [q['text']]
    if q['type'] in ('one', 'many'):
        content += [o['label'] + ') ' + o['text'] for o in q['options']]
    elif q['type'] == 'output':
        content += q['code'].splitlines()
    return ['> ' + line for line in content]

def answer_for(q, correct):
    if q['type'] in ('one', 'many'):
        right = [o['label'] for o in q['options'] if o['correct']]
        if correct:
            return ' '.join(right)
        if q['type'] == 'many':
            return right[0]
        return next(o['label'] for o in q['options'] if not o['correct'])
    answer = q['options'][0]['text'] if q['type'] == 'short' else q['expected'].strip()
    if correct:
        return answer
    for candidate in ('0', '1', '-1', 'ValueError', answer + '?'):
        if check(q, candidate) == 'неверно':
            return candidate
    candidate = answer + '?'
    while check(q, candidate) != 'неверно':
        candidate += '?'
    return candidate

def scan(bank):
    qs = bank['questions']
    out = [f'всего | {bank["total"]}', f'битых | {bank["broken"]}',
           f'вне шкалы | {sum(q["scale"] == 0 for q in qs)}']
    out += [f'уровень {n} | {sum(q["level"] == n for q in qs)}' for n in range(1, 6)]
    out += [f'тема {t} | {sum(q["topic"] == t for q in qs)}' for t in TOPICS]
    out += [f'тип {t} | {sum(q["type"] == t for q in qs)}' for t in TYPES]
    return '\n'.join(out) + '\n'

def bank_check(path, manifest_path):
    path = Path(path)
    manifest = json.loads(Path(manifest_path).read_text(encoding='utf-8'))
    rows, answers = raw(path)
    problems = []
    bank = load(path)
    if bank['broken']:
        problems.append(f'Структурно битых вопросов: {bank["broken"]}')
    ids = {ident for _, ident, _, _ in rows}
    for group, ident, p, line in rows:
        if group == 'team':
            if ident is None or ident < 1000:
                problems.append('ID команды должен быть от 1000')
            continue
        item = manifest.get(str(ident))
        if item is None or item['group'] != group:
            problems.append(f'Неизвестный исходный ID/группа: {ident}')
            continue
        snippets = {}
        for ext in ('py', 'out'):
            fn = f'{ident}.{ext}'
            if (path / 'snippets' / fn).exists():
                snippets[fn] = (path / 'snippets' / fn).read_text(encoding='utf-8')
        payload = {'question': line, 'answers': [a[2] for a in answers.get(ident, [])], 'snippets': snippets}
        digest = hashlib.sha256(json.dumps(payload, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
        if digest != item['sha256']:
            problems.append(f'Исходный вопрос {ident} изменён: разрешено только полное удаление из review')
    for ident, item in manifest.items():
        if item['group'] == 'reference' and int(ident) not in ids:
            problems.append(f'Удалён эталонный вопрос {ident}')
        if int(ident) not in ids:
            for ext in ('py', 'out'):
                if (path / 'snippets' / f'{ident}.{ext}').exists():
                    problems.append(f'Остался фрагмент удалённого вопроса {ident}.{ext}')
    if any(ident not in ids for ident in answers):
        problems.append('Есть строки ответов без вопроса')
    output_ids = {q['id'] for q in bank['questions'] if q['type'] == 'output'}
    for fragment in sorted((path / 'snippets').glob('*')):
        if fragment.suffix not in ('.py', '.out'):
            continue
        if not fragment.stem.isdigit() or int(fragment.stem) not in output_ids:
            problems.append(f'Фрагмент без исправного output-вопроса: {fragment.name}')
    team = [q for q in bank['questions'] if q['id'] >= 1000]
    if len(team) != 20:
        problems.append(f'Нужно 20 исправных вопросов команды; сейчас {len(team)}')
    if {q['type'] for q in team} != set(TYPES):
        problems.append('В банке команды должны встретиться четыре типа')
    if sum(q['scale'] == 0 for q in team) != 2:
        problems.append('В двадцать вопросов команды входят ровно два вне шкалы')
    return problems

def fixture(path):
    path = Path(path); (path / 'snippets').mkdir(parents=True, exist_ok=True)
    records = ['11 | ввод | 1 | one | 1 | Выберите число два.',
               '12 | данные | 3 | many | 1 | Выберите чётные числа.',
               '13 | ошибки | 2 | short | 1 | Назовите ValueError.',
               '14 | структура | 4 | output | 1 | Что напечатает код?',
               '15 | ввод |  | short | 0 | Скажите привет.']
    answers = ['11 | А | 1 | 2', '11 | Б | 0 | 3',
               '12 | А | 1 | 2', '12 | Б | 1 | 4', '12 | В | 0 | 3',
               '13 | - | 1 | ValueError', '15 | - | 1 | привет']
    (path / 'bank_reference.txt').write_text('\n'.join(records)+'\n', encoding='utf-8')
    (path / 'answers_reference.txt').write_text('\n'.join(answers)+'\n', encoding='utf-8')
    (path / 'snippets/14.py').write_text('print(1, 2)\n', encoding='utf-8')
    (path / 'snippets/14.out').write_text('1 2\n', encoding='utf-8')
    for name in ('bank_review', 'answers_review'):
        (path / (name + '.txt')).write_text('', encoding='utf-8')
