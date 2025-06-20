from typing import Any

from src.widget import get_date


def filter_by_state(transactions_list: list[dict[str, Any]], state: str = "EXECUTED") -> list | str:
    """Функция для отслеживания статуса"""
    if not transactions_list:
        return "Данные отсутствуют"
    state_filter = []
    for item in transactions_list:
        if item.get("state"):
            if item["state"] == state:
                state_filter.append(item)
        else:
            return "Отсутствует статус"
    if not state_filter:
        return "Отсутствует статус"
    return state_filter


def sort_by_date(transactions_list: list[dict[str, Any]], desc: bool = True) -> list | str:
    """Функция для сортировки по дате"""
    if not transactions_list:
        return "Данные отсутствуют"
    filtered_list = []
    for item in transactions_list:
        if item.get("date"):
            if get_date(item["date"]) == "Некорректная дата":
                continue
            filtered_list.append(item)
    if not filtered_list:
        return "Некорректная дата"
    return sorted(filtered_list, key=lambda i: i["date"], reverse=desc)


print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
