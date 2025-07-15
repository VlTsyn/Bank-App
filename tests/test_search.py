import pytest

from src.search import process_bank_operations, process_bank_search


@pytest.fixture
def operations():
    return [
        {
            "id": 509552992,
            "state": "EXECUTED",
            "date": "2019-04-19T12:02:30.129240",
            "operationAmount": {"amount": "81513.74", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод с карты на карту",
            "from": "Maestro 9171987821259925",
            "to": "МИР 2052809263194182",
        },
        {
            "id": 596914981,
            "state": "EXECUTED",
            "date": "2018-04-16T17:34:19.241289",
            "operationAmount": {"amount": "65169.27", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1813166339376336",
            "to": "Счет 97848259954268659635",
        },
        {
            "id": 200634844,
            "state": "CANCELED",
            "date": "2018-02-13T04:43:11.374324",
            "operationAmount": {"amount": "42210.20", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Счет 33355011456314142963",
            "to": "Счет 45735917297559088682",
        },
    ]


@pytest.fixture
def categories():
    return ["Перевод организации", "Перевод с карты на карту", "Открытие вклада"]


def test_process_bank_search(operations):
    result = process_bank_search(operations, "орг")
    assert result == [
        {
            "id": 596914981,
            "state": "EXECUTED",
            "date": "2018-04-16T17:34:19.241289",
            "operationAmount": {"amount": "65169.27", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1813166339376336",
            "to": "Счет 97848259954268659635",
        },
        {
            "id": 200634844,
            "state": "CANCELED",
            "date": "2018-02-13T04:43:11.374324",
            "operationAmount": {"amount": "42210.20", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Счет 33355011456314142963",
            "to": "Счет 45735917297559088682",
        },
    ]


def test_process_bank_operations(operations, categories):
    result = process_bank_operations(operations, categories)
    assert result == {"Перевод организации": 2, "Перевод с карты на карту": 1, "Открытие вклада": 0}
