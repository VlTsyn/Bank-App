import pytest

from src.widget import get_date, mask_account_card


def test_mask_card():
    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"


def test_mask_account():
    assert mask_account_card("Счет 64686473678894779589") == "Счет **9589"


@pytest.mark.parametrize(
    "info, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_account_or_card(info, expected):
    assert mask_account_card(info) == expected


@pytest.fixture
def info_error():
    return "Некорректный номер карты/счета"


@pytest.mark.parametrize(
    "info",
    [
        "Maestro 1596837",
        "Счет 64686473sdghhg779589",
        "MasterCard 71583007347267582345345113234",
        "Счет 353835560",
        "Visa Classic 6831()-*+=_)7658",
        "Visa Platinum ewyrutiylioippoi",
        "Visa 1234 5654 4897 7984",
        "Счет",
        "",
    ],
)
def test_correct_mask_account_card(info, info_error):
    assert mask_account_card(info) == info_error


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


@pytest.fixture
def date_error():
    return "Некорректная дата"


@pytest.mark.parametrize(
    "date",
    [
        "20240311T02:26:18.671407",
        "2024-03-T02:26:18.671407",
        "20-03-11T02:26:18.671407",
        "671407",
        "02:26:18",
        "asfdgfhdgjfh",
        "asda-as-weT02:26:18.671407",
        "2024-03-11qweretsThdtj",
        "2024-03-1102:26T:18.671407",
        "",
    ],
)
def test_correct_date(date, date_error):
    assert get_date(date) == date_error
