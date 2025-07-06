import json
from unittest.mock import mock_open, patch

import pytest

from src.utils import get_json_file


@pytest.fixture
def temp_json_file(tmp_path):
    data = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
    ]
    file_path = tmp_path / "sample.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    return file_path


def test_get_json_file(temp_json_file):
    data = get_json_file(temp_json_file)
    assert len(data) == 2
    assert data[0]["operationAmount"]["amount"] == "31957.58"
    assert data[1]["operationAmount"]["amount"] == "8221.37"


@pytest.fixture
def temp_empty_json_file(tmp_path):
    data = None
    file_path = tmp_path / "empty.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    return file_path


def test_get_empty_json_file(temp_empty_json_file):
    data = get_json_file(temp_empty_json_file)
    assert data == []


@pytest.fixture
def temp_dict_json_file(tmp_path):
    data = {"data": "test"}
    file_path = tmp_path / "dict.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    return file_path


def test_get_dict_json_file(temp_dict_json_file):
    data = get_json_file(temp_dict_json_file)
    assert data == []


def test_not_found_json_file():
    data = get_json_file("notfound.json")
    assert data == []


def test_json_decode_error():
    invalid_json = '{"data": "test"'
    with patch("builtins.open", mock_open(read_data=invalid_json)):
        data = get_json_file("invalid.json")
        assert data == []
