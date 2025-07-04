import json
from pathlib import Path


def get_json_file(file_path: str | Path) -> list[dict]:
    """Функция открытия JSON-файла"""
    try:
        with open(file_path, encoding="utf-8") as f:
            operations = json.load(f)

        if not isinstance(operations, list):
            return []

        return operations
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
