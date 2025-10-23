def filter_by_currency(transactions_list: list[dict], code: str = "USD") -> iter:
    """Функция, поочередно возвращающая транзакции по указанной валюте"""
    if not transactions_list:
        return "Данные отсутствуют"
    if not list(filter(lambda x: x["operationAmount"]["currency"]["code"] == code, transactions_list)):
        return "Некорректная валюта"
    currency_transactions = list(filter(lambda x: x["operationAmount"]["currency"]["code"] == code, transactions_list))
    for transaction in currency_transactions:
        yield transaction


def transaction_descriptions(transactions_list: list[dict]) -> iter:
    """Функция, поочередно возвращающая описание транзакций"""
    if not transactions_list:
        return "Данные отсутствуют"
    for transaction in transactions_list:
        yield transaction["description"]


def card_number_generator(start: int | str = 1, stop: int | str = 9999999999999999) -> iter:
    """Функция-генератор номера карты"""
    base_number = "0000000000000000"
    if int(start) > 0 and int(stop) > start and len(str(start)) <= 16 and len(str(stop)) <= 16:
        generation_number = start
        while int(generation_number) <= int(stop):
            final_number = base_number[: 16 - len(str(generation_number))] + str(generation_number)
            yield f"{final_number[:4]} {final_number[4:8]} {final_number[8:12]} {final_number[12:16]}"
            generation_number += 1
    else:
        return "Ошибка данных"
