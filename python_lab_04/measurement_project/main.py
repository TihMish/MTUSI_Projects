import json
import logging
from pathlib import Path

from utils.reader import read_numbers, validate_numbers
from utils.statistics import calculate_average, find_min, find_max


def main():
    with open("config.json", "r", encoding="utf-8") as file:
        config = json.load(file)
    path = Path(config["input_file"])
    Path("logs").mkdir(exist_ok=True)
    logging.basicConfig(filename=config["log_file"], level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", encoding="utf-8")
    logging.info("Программа запущена")
    print("Текущий каталог:", Path.cwd())
    print("Файл существует:", path.exists())
    try:
        numbers = read_numbers(path)
        validate_numbers(numbers)
    except FileNotFoundError:
        print("Файл не найден:", path)
        logging.error("Файл не найден: %s", path)
    except ValueError as e:
        print("Ошибка данных:", e)
        logging.error("Ошибка данных: %s", e)
    else:
        logging.info("Файл %s прочитан", path)
        logging.info("Прочитано значений: %d", len(numbers))
        print("Значений:", len(numbers), "Мин:", find_min(numbers), "Макс:", find_max(numbers), "Среднее:", calculate_average(numbers))
    finally:
        logging.info("Программа завершена")


if __name__ == "__main__":
    main()
