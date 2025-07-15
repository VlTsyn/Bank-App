import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    pattern = re.compile(search, re.IGNORECASE)
    return [d for d in data if d.get("description") and pattern.search(d["description"])]


def process_bank_operations(data: list[dict], categories: list) -> dict:
    matches = [category for d in data for category in categories if category.lower() in d.get("description").lower()]
    result = Counter({category: 0 for category in categories})
    result.update(matches)
    return dict(result)
