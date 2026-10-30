# -*- coding: utf-8 -*-
"""Сверка твоих выводов с фактами инцидента. Выдан готовым, менять его не нужно.

    python3 src/partner/verify.py

Запускает src/report.py, берёт четыре строки его вывода и сверяет их с контрольными
суммами. Печатает только «сходится» или «не сходится». Правильные значения не
показывает никогда — ни тебе, ни проверяющему.
"""
import hashlib, re, subprocess, sys
from pathlib import Path

КОРЕНЬ = Path(__file__).resolve().parents[2]
ОТЧЁТ = КОРЕНЬ / "src/report.py"

ПУНКТЫ = [("первый подозрительный вызов", "первый_подозрительный_вызов", False),
          ("отменено чужих заказов", "отменено_чужих_заказов", True),
          ("аккаунт выгодоприобретателя", "аккаунт_выгодоприобретателя", False),
          ("оформлено на этот аккаунт", "оформлено_на_один_аккаунт", True)]

def мой_вариант():
    """Буква варианта из src/variant.txt. Её выдают на бумажной карточке помощника."""
    файл = КОРЕНЬ / "src/variant.txt"
    if not файл.exists():
        raise SystemExit(
            "Не найден файл src/variant.txt.\n"
            "Возьми бумажную карточку помощника, найди на ней букву варианта\n"
            "и создай файл src/variant.txt с одной этой буквой внутри.")
    буква = файл.read_text(encoding="utf-8").strip().upper()[:1]
    if not (КОРЕНЬ / "datasets" / буква).exists():
        raise SystemExit(f"Варианта {буква!r} нет. Впиши в src/variant.txt букву с карточки.")
    return буква

def посолить(логин, значение):
    основа = f"lavka-2026|{логин}|{str(значение).strip().lower()}"
    return hashlib.sha256(основа.encode("utf-8")).hexdigest()[:16]

def main():
    if not ОТЧЁТ.exists():
        print("Файла src/report.py нет. Сначала напиши его: см. Задание 4 в README.")
        raise SystemExit(1)
    логин = мой_вариант()
    суммы = {}
    for строка in (КОРЕНЬ / "datasets" / логин / "answers.sha256").read_text(
            encoding="utf-8").splitlines():
        if строка.startswith("#") or ":" not in строка:
            continue
        поле, значение = строка.split(":", 1)
        суммы[поле.strip()] = значение.strip()

    запуск = subprocess.run([sys.executable, str(ОТЧЁТ)], capture_output=True,
                            text=True, timeout=120, cwd=str(КОРЕНЬ))
    if запуск.returncode != 0:
        print("src/report.py завершился с ошибкой:\n")
        print((запуск.stderr or "").strip()[-600:])
        raise SystemExit(1)

    ответы = {}
    for строка in запуск.stdout.splitlines():
        if ":" in строка:
            ключ, значение = строка.split(":", 1)
            ответы[ключ.strip().lower()] = значение.strip()

    print(f"Вариант {логин}. Сверяю выводы с фактами инцидента.\n")
    сошлось = 0
    for подпись, поле, это_число in ПУНКТЫ:
        дано = ответы.get(подпись)
        if дано is None:
            print(f"  ? {подпись}: строки с таким началом в выводе нет")
            continue
        нормализованное = re.sub(r"\D", "", дано) if это_число else дано
        совпало = посолить(логин, нормализованное) == суммы.get(поле)
        print(f"  {'+' if совпало else '-'} {подпись}: {'сходится' if совпало else 'не сходится'}")
        сошлось += совпало
    print(f"\nСошлось пунктов: {сошлось} из {len(ПУНКТЫ)}")
    print("Правильные значения этот скрипт не показывает.")

if __name__ == "__main__":
    main()
