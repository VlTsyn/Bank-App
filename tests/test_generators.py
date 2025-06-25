import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def usd_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]


@pytest.fixture
def rub_transactions():
    return [
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.mark.parametrize("code, expected_result", [("USD", "usd_transactions"), ("RUB", "rub_transactions")])
def test_transactions(request, transactions, code, expected_result):
    filtered_transactions = filter_by_currency(transactions, code)
    result = []
    try:
        while True:
            result.append(next(filtered_transactions))
    except StopIteration as e:
        print(e.value)
    assert request.getfixturevalue(expected_result) == result


def test_transactions_empty():
    filtered_transactions = filter_by_currency([])
    try:
        next(filtered_transactions)
    except StopIteration as e:
        assert e.value == "Данные отсутствуют"


def test_incorrect_code(transactions):
    filtered_transactions = filter_by_currency(transactions, "gfs")
    try:
        next(filtered_transactions)
    except StopIteration as e:
        assert e.value == "Некорректная валюта"


def test_transaction_descriptions(transactions):
    description = transaction_descriptions(transactions)
    assert next(description) == "Перевод организации"
    assert next(description) == "Перевод со счета на счет"
    assert next(description) == "Перевод со счета на счет"
    assert next(description) == "Перевод с карты на карту"
    assert next(description) == "Перевод организации"


def test_transactions_desc_empty():
    description = transaction_descriptions([])
    try:
        next(description)
    except StopIteration as e:
        assert e.value == "Данные отсутствуют"


def test_card_number_generator():
    number_generator = card_number_generator(123456)
    assert next(number_generator) == "0000 0000 0012 3456"
    assert next(number_generator) == "0000 0000 0012 3457"
    assert next(number_generator) == "0000 0000 0012 3458"


def test_wrong_start_number():
    wrong_start = card_number_generator(0)
    try:
        next(wrong_start)
    except StopIteration as e:
        assert e.value == "Ошибка данных"


def test_wrong_stop_number():
    wrong_stop = card_number_generator(100, 50)
    try:
        next(wrong_stop)
    except StopIteration as e:
        assert e.value == "Ошибка данных"


def test_wrong_len_start_number():
    wrong_len_start = card_number_generator(12345678901234567)
    try:
        next(wrong_len_start)
    except StopIteration as e:
        assert e.value == "Ошибка данных"


def test_wrong_len_stop_number():
    wrong_len_stop = card_number_generator(456, 12345678901234567)
    try:
        next(wrong_len_stop)
    except StopIteration as e:
        assert e.value == "Ошибка данных"
