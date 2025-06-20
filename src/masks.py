from typing import Optional


def get_mask_card_number(card_number: Optional[int] = None) -> str:
    """Функция маскировки номера банковской карты"""
    if len(str(card_number)) != 16 or not str(card_number).isdigit():
        return "Некорректный номер карты"

    return f"{str(card_number)[:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}"


def get_mask_account(account_number: Optional[int] = None) -> str:
    """Функция маскировки номера банковского счета"""
    if len(str(account_number)) != 20 or not str(account_number).isdigit():
        return "Некорректный номер счета"

    return f"**{str(account_number)[-4:]}"
