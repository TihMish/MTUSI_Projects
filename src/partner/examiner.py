#!/usr/bin/env python3
"""Локальный открытый проверяющий. Только стандартная библиотека Python."""
import argparse
import json
import os
from pathlib import Path
import random
import re
import secrets
import selectors
import shutil
import subprocess
import sys
import tempfile
import time

import checklib as C

HERE = Path(__file__).resolve().parent
VERDICT = re.compile(r'(УРОВЕНЬ ([1-5])|НЕ ОПРЕДЕЛЁН) \| ВОПРОСОВ ([0-9]+) \| УВЕРЕННОСТЬ (0\.[0-9]{2}|1\.00)')
QUESTION = re.compile(r'([0-9]+) \| вопрос ([0-9]+) \| уровень ([1-5]|-) \| тема (\S+) \| тип (\S+) \| в_шкале ([01])')
ANSWER = re.compile(r'([0-9]+) \| ответ (.+) \| (верно|неверно|не принят) \| дальше (уровень [1-5-]|стоп)')
REASONS = {'сошлось', 'бюджет', 'вопросов нет', 'конец ввода'}

def run_session(main, bankpath, level, seed, profile='ideal', verbose=False):
    bank = {q['id']: q for q in C.load(bankpath)['questions']}
    proc = subprocess.Popen([sys.executable, str(Path(main).resolve()), str(Path(bankpath).resolve()),
                             '--seed', str(seed)], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, bufsize=0, cwd=Path(main).resolve().parent.parent)
    sel = selectors.DefaultSelector()
    sel.register(proc.stdout, selectors.EVENT_READ, 'out')
    sel.register(proc.stderr, selectors.EVENT_READ, 'err')
    buffers = {'out': b'', 'err': b''}; transcript = {'out': [], 'err': []}
    pending = None; prompt = False; sent = False; sent_value = None
    trace = []; statuses = []; result = None; reason = None
    last_following = None; block = []
    rng = random.Random(seed + 937 * level)
    started = time.monotonic(); input_closed = False
    try:
        while sel.get_map():
            if time.monotonic() - started > 8:
                raise ValueError('Таймаут 8 с: проверьте flush=True и условия остановки')
            for key, _ in sel.select(0.05):
                name = key.data
                chunk = os.read(key.fd, 65536)
                if not chunk:
                    sel.unregister(key.fileobj)
                    if buffers[name]:
                        raise ValueError('Вывод без завершающего перевода строки')
                    continue
                buffers[name] += chunk
                if sum(map(len, buffers.values())) > 200000:
                    raise ValueError('Слишком большой вывод без перевода строки')
                while b'\n' in buffers[name]:
                    raw, buffers[name] = buffers[name].split(b'\n', 1)
                    line = raw.decode('utf-8')
                    transcript[name].append(line)
                    if len(transcript[name]) > 10000:
                        raise ValueError('Слишком большой вывод')
                    if verbose:
                        print(name + '> ' + line)
                    if name == 'out':
                        if result is not None:
                            raise ValueError('Вердикт должен быть последней строкой stdout')
                        match = VERDICT.fullmatch(line)
                        if match:
                            result = (int(match[2]) if match[2] else None, int(match[3]), float(match[4]))
                        elif line == 'ОТВЕТ:':
                            if prompt:
                                raise ValueError('Повторный маркер ОТВЕТ:')
                            prompt = True
                        else:
                            if not line.startswith('> '):
                                raise ValueError('Строка содержимого stdout должна начинаться с > и пробела')
                            block.append(line)
                    else:
                        qm = QUESTION.fullmatch(line)
                        am = ANSWER.fullmatch(line)
                        if reason is not None:
                            raise ValueError('После строки остановки появились новые строки stderr')
                        if qm:
                            if pending is not None:
                                raise ValueError('Новый вопрос до завершения предыдущего')
                            if last_following == 'стоп':
                                raise ValueError('Новый вопрос после решения дальше стоп')
                            step, ident = int(qm[1]), int(qm[2])
                            if step != len(trace) + 1 or step > 20 or ident in [t['id'] for t in trace]:
                                raise ValueError('Неверный шаг, повтор вопроса или превышение бюджета')
                            if ident not in bank:
                                raise ValueError('Предъявлен битый или отсутствующий вопрос')
                            q = bank[ident]
                            expected = (str(q['level']) if q['level'] is not None else '-', q['topic'], q['type'], str(q['scale']))
                            if tuple(qm.group(i) for i in (3,4,5,6)) != expected:
                                raise ValueError('Атрибуты вопроса в логе не соответствуют банку')
                            pending=q; sent=False; trace.append(q)
                        elif am:
                            if pending is None or not sent or int(am[1]) != len(trace):
                                raise ValueError('Строка ответа без вопроса/ввода')
                            value = json.loads(am[2])
                            if value != sent_value or am[3] != C.check(pending, value):
                                raise ValueError('Неверная запись/классификация ответа в логе')
                            last_following = am[4]
                            statuses.append((pending, am[3])); pending=None
                        elif line.startswith('стоп | причина '):
                            if reason is not None or line[15:] not in REASONS:
                                raise ValueError('Неверная или повторная причина остановки')
                            reason=line[15:]
                        else:
                            raise ValueError('Неизвестная строка stderr: ' + line[:150])
            if pending is not None and prompt and not sent:
                q = pending
                if block != C.presentation(q):
                    raise ValueError('Предъявление отличается от банка: проверьте текст, пары метка–вариант и код')
                block = []
                correct = q['level'] is None or q['level'] <= level
                if profile == 'guesser' and not correct and q['type'] in ('one','many'):
                    correct = rng.random() < 0.25
                if profile == 'inattentive' and correct:
                    correct = rng.random() >= 0.15
                if profile == 'tired' and len(trace) > 5 and correct:
                    correct = rng.random() >= 0.35
                if profile == 'inverted' and q['level'] is not None:
                    correct = q['level'] >= 4
                if profile == 'eof' or (profile == 'mixed' and len(trace) >= 4):
                    proc.stdin.close(); input_closed=True; sent_value=None
                else:
                    sent_value = '' if profile == 'empty' else C.answer_for(q, correct)
                    if profile == 'mixed' and len(trace) in (2, 3):
                        sent_value = '' if len(trace) == 2 else '   '
                    proc.stdin.write((sent_value + '\n').encode()); proc.stdin.flush()
                sent=True; prompt=False
        code = proc.wait(timeout=1)
        if code != 0 or result is None or reason is None or pending is not None or prompt or block:
            raise ValueError('Нет полного корректного завершения: код/вердикт/лог')
        if result[1] != len(trace) or len(statuses) != len(trace):
            raise ValueError('Счётчик вопросов не соответствует логу')
        if input_closed and reason != 'конец ввода':
            raise ValueError('EOF требует причины конец ввода')
        if not input_closed and reason == 'конец ввода':
            raise ValueError('Причина конец ввода без полученного EOF')
        if trace and last_following != 'стоп':
            raise ValueError('Последняя строка ответа должна сообщать дальше стоп')
        if reason == 'бюджет' and len(trace) != 20:
            raise ValueError('Причина бюджет допустима только при 20 вопросах')
        if not trace and reason != 'вопросов нет':
            raise ValueError('Остановка без вопросов требует причины вопросов нет')
        evidence = [(q,s) for q,s in statuses if q['scale'] and s != 'не принят']
        if not evidence and (result[0] is not None or result[2] != 0):
            raise ValueError('Без свидетельств требуется НЕ ОПРЕДЕЛЁН и уверенность 0.00')
        return {'level':result[0], 'count':result[1], 'confidence':result[2],
                'levels':[q['level'] for q in trace], 'transcript':transcript}
    finally:
        if proc.poll() is None:
            proc.kill(); proc.wait()
        sel.close()
        for stream in (proc.stdin, proc.stdout, proc.stderr):
            if stream and not stream.closed:
                stream.close()

def call(main, args):
    proc=subprocess.run([sys.executable,str(Path(main).resolve())]+args,
                        cwd=Path(main).resolve().parent.parent,capture_output=True,text=True,timeout=8)
    if proc.returncode:
        raise ValueError(proc.stderr.strip() or 'Программа завершилась ненулевым кодом')
    return proc.stdout

def task1(main):
    with tempfile.TemporaryDirectory(prefix='dopusk_scan_') as tmp:
        p=Path(tmp); C.fixture(p)
        for extra in ('', '16 | ввод | 1 | one | 1 | Нет ответов.\n',
                      '17 | ввод | 9 | unknown | 1 | Неверные поля.\n',
                      '11 | ввод | 1 | one | 1 | Дубликат.\n'):
            (p/'bank_review.txt').write_text(extra,encoding='utf-8')
            actual=call(main,[tmp,'--scan'])
            if actual != C.scan(C.load(p)):
                raise ValueError('Разведочный вывод не совпал с эталоном на малом банке')

def task2(main):
    code = '''import sys,json
sys.path.insert(0,sys.argv[1])
import bank
qs={q['id']:q for q in bank.load(sys.argv[2])['questions']}
tests=json.loads(sys.argv[3])
print(json.dumps([bank.check(qs[i],a) for i,a in tests],ensure_ascii=False))
'''
    tests=[(11,'А'),(11,'б'),(11,'Z'),(11,''),(11,'   '),(11,'А Б'),(11,None),
           (12,'Б А'),(12,'А'),(12,'А А Б'),(12,'В'),(12,'А Ж'),(12,None),
           (13,' valueerror '),(13,'TypeError'),(13,'"текст" | кавычки'),
           (14,'1 2'),(14,'1  2'),(14,''),(14,None),(15,None)]
    with tempfile.TemporaryDirectory(prefix='dopusk_answers_') as tmp:
        C.fixture(tmp); qs={q['id']:q for q in C.load(tmp)['questions']}
        expected=[C.check(qs[i],a) for i,a in tests]
        proc=subprocess.run([sys.executable,'-c',code,str(Path(main).resolve().parent),tmp,
                             json.dumps(tests)],capture_output=True,text=True,timeout=8)
        if proc.returncode or json.loads(proc.stdout) != expected:
            raise ValueError('bank.load / bank.check не прошли проверку типов: '+proc.stderr[-300:])

def explain_contract(main, bank):
    """--explain обязателен: он не меняет stdout и добавляет объяснение в stderr."""
    base=[sys.executable,str(Path(main).resolve()),str(Path(bank).resolve()),'--seed','4711']
    where=Path(main).resolve().parent.parent
    plain=subprocess.run(base,input='',capture_output=True,text=True,timeout=8,cwd=where)
    rich=subprocess.run(base+['--explain'],input='',capture_output=True,text=True,timeout=8,cwd=where)
    if plain.returncode or rich.returncode:
        raise ValueError('Запуск с --explain и без него должен завершаться кодом 0')
    if plain.stdout != rich.stdout:
        raise ValueError('--explain изменил stdout: объяснение выводится только в stderr')
    if 'ОБЪЯСНЕНИЕ:' in plain.stderr:
        raise ValueError('Строки ОБЪЯСНЕНИЕ: появились без флага --explain')
    if 'ОБЪЯСНЕНИЕ:' not in rich.stderr:
        raise ValueError('--explain не добавил ни одной строки ОБЪЯСНЕНИЕ: в stderr')

def task3(main, bank):
    a=run_session(main,bank,3,4711)
    b=run_session(main,bank,3,4711)
    if a['transcript'] != b['transcript']:
        raise ValueError('Одинаковый seed, банк и ответы дали разный вывод')
    run_session(main,bank,3,4711,'eof')
    run_session(main,bank,3,4711,'empty')
    run_session(main,bank,3,4711,'mixed')
    with tempfile.TemporaryDirectory(prefix='dopusk_empty_') as tmp:
        p=Path(tmp)
        (p/'bank_reference.txt').write_text('',encoding='utf-8')
        (p/'bank_review.txt').write_text('',encoding='utf-8')
        (p/'bank_team.txt').write_text('',encoding='utf-8')
        run_session(main,p,3,4711)
    explain_contract(main,bank)

def observation_contract(main):
    code = '''import sys, json, copy
sys.path.insert(0, sys.argv[1])
import engine
qs=json.loads(sys.argv[2])
state=engine.start()
assert isinstance(state,dict), 'engine.start должен вернуть словарь'
other=engine.start()
assert isinstance(other,dict) and other is not state, 'start должен создавать новый словарь'
def valid(value):
    if isinstance(value,dict):
        assert all(isinstance(k,str) for k in value), 'Ключи state должны быть строками'
        for v in value.values(): valid(v)
    elif isinstance(value,list):
        for v in value: valid(v)
    else:
        assert value is None or isinstance(value,(str,int,float,bool)), 'state должен быть JSON-совместим'
    json.dumps(value,allow_nan=False)
valid(state)
initial=copy.deepcopy(other)
assert engine.observe(state,qs[0],'верно') is None
assert other==initial, 'Состояния двух сессий связаны'
for warmup in ([],[(qs[0],'верно')],[(qs[1],'верно')]):
    state=engine.start()
    for q,status in warmup:
        assert engine.observe(state,q,status) is None, 'observe изменяет state и возвращает None'
    for q,status in [(qs[1],'не принят'),(qs[0],'не принят'),(qs[4],'верно'),(qs[4],'неверно')]:
        before=copy.deepcopy(state)
        assert engine.observe(state,q,status) is None, 'observe должен вернуть None'
        valid(state)
        assert state==before, 'Не принят / вне шкалы изменили состояние знаний'
print('СОСТОЯНИЕ: ОК')
'''
    with tempfile.TemporaryDirectory(prefix='dopusk_state_') as tmp:
        C.fixture(tmp)
        questions=C.load(tmp)['questions']
        proc=subprocess.run([sys.executable,'-c',code,str(Path(main).resolve().parent),
                             json.dumps(questions,ensure_ascii=False)],capture_output=True,text=True,timeout=8)
        if proc.returncode or proc.stdout.strip()!='СОСТОЯНИЕ: ОК':
            raise ValueError('engine.start / observe: '+(proc.stderr.strip() or proc.stdout.strip())[-600:])

def task4(main, bank, key):
    observation_contract(main)
    seeds=[key*100+offset for offset in (11,23,37)]
    results=[]
    for seed in seeds:
        group=[]
        for level in range(1,6):
            r=run_session(main,bank,level,seed)
            if r['level'] != level:
                raise ValueError(f'Эталон {level}, seed {seed}: получен {r["level"]}')
            group.append(tuple(r['levels'])); results.append(r)
        if len(set(group)) == 1:
            raise ValueError('Сложность и длина сессии не зависят от ответов')
    with tempfile.TemporaryDirectory(prefix='dopusk_stress_') as tmp:
        for mode in ('missing_level','missing_topic','broken'):
            dest=Path(tmp)/mode; shutil.copytree(bank,dest)
            for file in dest.glob('bank_*.txt'):
                retained=[]
                for line in file.read_text(encoding='utf-8').splitlines():
                    parts=[x.strip() for x in line.split('|')]
                    drop=len(parts)==6 and ((mode=='missing_level' and parts[2]=='4') or
                                           (mode=='missing_topic' and parts[1]=='структура'))
                    if not drop: retained.append(line)
                file.write_text('\n'.join(retained)+'\n',encoding='utf-8')
            if mode=='broken':
                with (dest/'bank_review.txt').open('a',encoding='utf-8') as stream:
                    stream.write('998 | ввод | 2 | output | 1 | Нет фрагмента.\n')
            run_session(main,dest,4,seeds[0])
    print('эталонных сессий 15 | точность 1.00 | длина '+format(sum(r['count'] for r in results)/15,'.2f'))

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--task',type=int,choices=(1,2,3,4))
    parser.add_argument('--run',action='store_true')
    parser.add_argument('--play',nargs='?',const='list')
    parser.add_argument('--control',nargs='?',const='new',metavar='КЛЮЧ')
    parser.add_argument('--bank-check',metavar='ПАПКА')
    parser.add_argument('--seed',type=int,default=4711)
    parser.add_argument('paths',nargs='*')
    args=parser.parse_args()
    modes=sum([args.task is not None,args.run,args.play is not None,args.control is not None,args.bank_check is not None])
    if modes!=1: parser.error('Выберите ровно один режим')
    if args.control=='new':
        if args.paths: parser.error('--control без ключа не принимает пути')
        print(secrets.randbelow(900000)+100000); return 0
    profiles={'ровный-1':(1,'ideal'),'ровный-2':(2,'ideal'),'ровный-3':(3,'ideal'),
              'ровный-4':(4,'ideal'),'ровный-5':(5,'ideal'),'угадыватель':(1,'guesser'),
              'невнимательный':(4,'inattentive'),'уставающий':(4,'tired'),'перевёрнутый':(3,'inverted'),
              'смешанный-ввод':(3,'mixed')}
    if args.play=='list': print('\n'.join(profiles)); return 0
    if args.bank_check:
        issues=C.bank_check(args.bank_check,HERE/'bank_manifest.json')
        print('\n'.join(issues) if issues else 'Структура, количество и сохранность: ОК')
        print('БАНК НЕ ПРИНЯТ' if issues else 'СТРУКТУРА БАНКА ПРИНЯТА; содержание проверяет пир')
        return int(bool(issues))
    if len(args.paths)!=2: parser.error('Нужны путь к main.py и папка банка')
    entry,bank=args.paths
    if args.play:
        if args.play not in profiles: parser.error('Неизвестный профиль')
        level,kind=profiles[args.play]
        result=run_session(entry,bank,level,args.seed,kind,True)
        print(f'профиль {args.play} | уровень {result["level"]} | вопросов {result["count"]} | уверенность {result["confidence"]:.2f}')
        return 0
    key=args.seed if args.control is None else int(args.control)
    tasks=[args.task] if args.task else [1,2,3,4]
    failed=False
    for number in tasks:
        try:
            if number==1: task1(entry)
            elif number==2: task2(entry)
            elif number==3: task3(entry,bank)
            else: task4(entry,bank,key)
            print(f'ЭТАП {number}: ПРОЙДЕН')
        except (ValueError,OSError,subprocess.SubprocessError,KeyError,TypeError) as exc:
            failed=True; print(f'ЭТАП {number}: НЕ ПРОЙДЕН — {exc}')
    print('КОД НЕ ПРИНЯТ' if failed else 'КОД ПРИНЯТ')
    return int(failed)

if __name__=='__main__':
    try:
        sys.exit(main())
    except (ValueError,OSError,subprocess.SubprocessError) as exc:
        print('ОШИБКА ПРОВЕРКИ: '+str(exc),file=sys.stderr); sys.exit(1)
