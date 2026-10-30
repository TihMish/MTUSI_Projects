"""Линтер. Выданная программа, править нельзя.

Читает твой код, не запуская его, и показывает места, написанные небрежно.
Он не проверяет, верно ли считает программа.

    python3 src/partner/lint.py src

Проверяет каждый файл .py в указанной папке, кроме папки partner.
Молчит — значит замечаний нет.
"""

import ast
import os
import sys

LINE_LIMIT = 100


class Report:
    def __init__(self):
        self.items = []

    def add(self, path, line, code, text):
        self.items.append((path, line, code, text))


def check_long_lines(path, source, report):
    for number, line in enumerate(source.split("\n"), 1):
        if len(line) > LINE_LIMIT:
            report.add(path, number, "L001",
                       "строка длиннее %d символов" % LINE_LIMIT)
        if "\t" in line:
            report.add(path, number, "L002",
                       "табуляция в строке: отступы делаются пробелами")


def imported_names(tree):
    names = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for item in node.names:
                names[(item.asname or item.name).split(".")[0]] = node.lineno
        elif isinstance(node, ast.ImportFrom):
            for item in node.names:
                names[item.asname or item.name] = node.lineno
    return names


def used_names(tree):
    used = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            used.add(node.id)
        elif isinstance(node, ast.Attribute):
            target = node
            while isinstance(target, ast.Attribute):
                target = target.value
            if isinstance(target, ast.Name):
                used.add(target.id)
    return used


def imports_module(tree, module):
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            if any(item.name == module for item in node.names):
                return True
        elif isinstance(node, ast.ImportFrom) and node.module == module:
            return True
    return False


def check_unused_imports(path, tree, report):
    used = used_names(tree)
    for name, line in imported_names(tree).items():
        if name not in used:
            report.add(path, line, "L010",
                       "импорт «%s» не используется" % name)


def check_unused_variables(path, tree, report):
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        assigned = {}
        for inner in ast.walk(node):
            if isinstance(inner, ast.Assign):
                for target in inner.targets:
                    if isinstance(target, ast.Name):
                        assigned.setdefault(target.id, inner.lineno)
        used = used_names(node)
        loads = set()
        for inner in ast.walk(node):
            if isinstance(inner, ast.Name) and isinstance(inner.ctx, ast.Load):
                loads.add(inner.id)
        for name, line in assigned.items():
            if name.startswith("_"):
                continue
            if name not in loads:
                report.add(path, line, "L011",
                           "переменная «%s» заведена и не используется" % name)


def check_no_print(path, tree, report):
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id == "print":
                report.add(path, node.lineno, "L020",
                           "модуль не должен печатать: печатает точка входа")


def check_has_import(path, tree, report, module):
    if not imports_module(tree, module):
        report.add(path, 1, "L021",
                   "нет импорта модуля «%s»" % module)


def check_file(path, report):
    with open(path, encoding="utf-8") as source:
        text = source.read()
    check_long_lines(path, text, report)
    try:
        tree = ast.parse(text, filename=path)
    except SyntaxError as error:
        report.add(path, error.lineno or 1, "L000",
                   "файл не разбирается: %s" % error.msg)
        return
    check_unused_imports(path, tree, report)
    check_unused_variables(path, tree, report)
    name = os.path.basename(path)
    if name == "memory.py":
        check_no_print(path, tree, report)
    if name == "main.py":
        check_has_import(path, tree, report, "memory")


def collect(target):
    if os.path.isfile(target):
        return [target]
    found = []
    for folder, dirs, files in os.walk(target):
        dirs[:] = [d for d in dirs if d not in ("partner", "__pycache__")]
        for name in sorted(files):
            if name.endswith(".py"):
                found.append(os.path.join(folder, name))
    return found


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 1
    files = collect(sys.argv[1])
    if not files:
        print("Файлов .py не найдено: " + sys.argv[1])
        return 1
    report = Report()
    for path in files:
        check_file(path, report)
    for path, line, code, text in sorted(report.items):
        print("%s:%d: %s %s" % (path, line, code, text))
    if report.items:
        print("")
        print("Замечаний: %d" % len(report.items))
        return 1
    print("Замечаний нет.")
    return 0


sys.exit(main())
