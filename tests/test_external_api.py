import os
from unittest.mock import patch

import pytest
from dotenv import load_dotenv

from src.external_api import transaction_converter

load_dotenv()
API_KEY = os.getenv("API_KEY")
URL = os.getenv("URL")


@pytest.fixture
def transaction_rub():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "10000", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@pytest.fixture
def transaction_usd():
    return {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "1000", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }


@pytest.fixture
def transaction_eur():
    return {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "1000", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }


@patch("requests.request")
def test_transaction_converter_usd(mock_get, transaction_usd):
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 1000},
        "info": {"timestamp": 1751659505, "rate": 80},
        "date": "2025-07-04",
        "result": 80000,
    }
    assert transaction_converter(transaction_usd) == 80000
    mock_get.assert_called_once_with("GET", f"{URL}?to=RUB&from=USD&amount=1000", headers={"apikey": API_KEY}, data={})


@patch("requests.request")
def test_transaction_converter_eur(mock_get, transaction_eur):
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "EUR", "to": "RUB", "amount": 1000},
        "info": {"timestamp": 1751659505, "rate": 90},
        "date": "2025-07-04",
        "result": 90000,
    }
    assert transaction_converter(transaction_eur) == 90000
    mock_get.assert_called_once_with("GET", f"{URL}?to=RUB&from=EUR&amount=1000", headers={"apikey": API_KEY}, data={})


def test_def_test_transaction_rub(transaction_rub):
    assert transaction_converter(transaction_rub) == 10000
