import json
import logging
from pathlib import Path

logger = logging.getLogger("Utils.py")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/utils.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_json_file(file_path: str | Path) -> list[dict]:
    """Функция открытия JSON-файла"""
    try:
        logger.info("Открытие JSON файла")
        with open(file_path, encoding="utf-8") as f:
            operations = json.load(f)

        if not isinstance(operations, list):
            logger.warning("Не содержит список")
            return []

        logger.info("Завершение работы функции")
        return operations
    except FileNotFoundError:
        logger.error("Файл не найден")
        return []
    except json.JSONDecodeError:
        logger.error("Ошибка кодировки")
        return []
