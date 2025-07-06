import logging
from typing import Optional

logger = logging.getLogger("masks.py")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/masks.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Optional[int] = None) -> str:
    """Функция маскировки номера банковской карты"""
    logger.info("Проверка номера карты")
    if len(str(card_number)) != 16 or not str(card_number).isdigit():

        logger.error("Неверные данные")
        return "Некорректный номер карты"

    logger.info("Завершение работы функции")
    return f"{str(card_number)[:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}"


def get_mask_account(account_number: Optional[int] = None) -> str:
    """Функция маскировки номера банковского счета"""
    logger.info("Проверка номера счета")
    if len(str(account_number)) != 20 or not str(account_number).isdigit():

        logger.error("Неверные данные")
        return "Некорректный номер счета"

    logger.info("Завершение работы функции")
    return f"**{str(account_number)[-4:]}"
