import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_mask_number():
    assert get_mask_card_number(1234567890123456) == "1234 56** **** 3456"


@pytest.fixture
def card_error():
    return "Некорректный номер карты"


@pytest.mark.parametrize(
    "number",
    [
        0,
        1234567890,
        12345678901234567890,
        "1234 9012 1234 1234",
        "asdfghasdqwertyq",
        "123456789o123456",
        "1234()7_9+-2a4s6",
        "123456789  23456",
        "",
    ],
)
def test_len_card_number(number, card_error):
    assert get_mask_card_number(number) == card_error


def test_mask_account():
    assert get_mask_account(12345678901234567890) == "**7890"


@pytest.fixture
def account_error():
    return "Некорректный номер счета"


@pytest.mark.parametrize(
    "number",
    [
        0,
        1234567890,
        1234567890123456789012345,
        "1234 9012 1234 1234 ",
        "asdfghasdqwertyqqwer",
        "123456789o123456qwer",
        "1234()7_9+-2a4s6,.=!",
        "ewfesdgfdhgj",
        "",
    ],
)
def test_len_account_number(number, account_error):
    assert get_mask_account(number) == account_error
