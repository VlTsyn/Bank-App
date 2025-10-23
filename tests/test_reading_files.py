from unittest.mock import patch

import pandas as pd
import pytest

from src.reading_files import reading_from_csv, reading_from_excel


@pytest.fixture
def temp_df():
    data = [
        {
            "id": 650703,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 3598919,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 593027,
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "amount": 30368.0,
            "currency_name": "Shilling",
            "currency_code": "TZS",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
            "description": "Перевод с карты на карту",
        },
    ]
    return pd.DataFrame(data)


def test_reading_from_csv(temp_df):
    with patch("pandas.read_csv", return_value=temp_df) as read_csv_mock:
        data = reading_from_csv("test_file.csv")
        read_csv_mock.assert_called_once_with("test_file.csv", sep=";")
        assert data == temp_df.to_dict("records")


def test_reading_from_excel(temp_df):
    with patch("pandas.read_excel", return_value=temp_df) as read_excel_mock:
        data = reading_from_excel("test_file.xlsx")
        read_excel_mock.assert_called_once_with("test_file.xlsx")
        assert data == temp_df.to_dict("records")
