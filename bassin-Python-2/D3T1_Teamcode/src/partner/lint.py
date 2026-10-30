"""Минимальный воспроизводимый линтер проекта; внешние пакеты не нужны."""
import ast
from pathlib import Path
import sys


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('src')
    issues = []
    for path in sorted(root.glob('*.py')):
        text = path.read_text(encoding='utf-8')
        try:
            tree = ast.parse(text)
        except SyntaxError as exc:
            issues.append(f'{path}:{exc.lineno}: {exc.msg}')
            continue
        for number, line in enumerate(text.splitlines(), 1):
            if '\t' in line:
                issues.append(f'{path}:{number}: используйте пробелы вместо табуляции')
            if line.rstrip() != line:
                issues.append(f'{path}:{number}: пробелы в конце строки')
            if len(line) > 120:
                issues.append(f'{path}:{number}: строка длиннее 120 символов')
        if path.name in ('bank.py', 'engine.py'):
            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'print':
                    issues.append(f'{path}:{node.lineno}: модуль не должен печатать')
    print('\n'.join(issues) if issues else 'ЛИНТЕР: ОК')
    return int(bool(issues))


if __name__ == '__main__':
    sys.exit(main())
