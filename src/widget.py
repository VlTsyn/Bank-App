from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(information: str) -> str:
    """Функция маскировки номера банковской карты/счета"""
    number = information.split(" ")[-1]
    if len(number) == 16 and number.isdigit():
        return f"{' '.join(information.split(' ')[0:-1])} {get_mask_card_number(int(number))}"
    elif len(number) == 20 and number.isdigit():
        return f"{' '.join(information.split(' ')[0:-1])} {get_mask_account(int(number))}"
    else:
        return "Некорректный номер карты/счета"


def get_date(date: str) -> str:
    """Функция обработки даты"""
    if "T" in date:
        cut_date = date.split("T")
        if len(cut_date[0]) == 10:
            date_index = cut_date[0].split("-")
            for i in date_index:
                if not i.isdigit():
                    return "Некорректная дата"
                if len(date_index[0]) == 4 and (0 < int(date_index[1]) < 12) and (0 < int(date_index[2]) < 31):
                    return f"{date_index[2]}.{date_index[1]}.{date_index[0]}"
        return "Некорректная дата"
    return "Некорректная дата"
