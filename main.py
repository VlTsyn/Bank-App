from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.reading_files import reading_from_csv, reading_from_excel
from src.search import process_bank_search
from src.utils import get_json_file
from src.widget import get_date


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    file_type = input("Ввод: ")
    transactions_list = []

    if file_type == "1":
        print("Для обработки выбран JSON-файл.")
        transactions_list = get_json_file("data/operations.json")
    elif file_type == "2":
        print("Для обработки выбран CSV-файл.")
        transactions_list = reading_from_csv("data/transactions.csv")
    elif file_type == "3":
        print("Для обработки выбран XLSX-файл.")
        transactions_list = reading_from_excel("data/transactions_excel.xlsx")
    else:
        print("Некорректный выбор.Завершение работы программы")

    statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status = input("Статус: ").upper()

        if status in statuses:
            print(f"Операции отфильтрованы по статусу '{status}'")
            filtered_data = filter_by_state(transactions_list, status)
            break
        else:
            print(f"Статус операции '{status}' недоступен.")

    print("\nОтсортировать операции по дате?")
    sort_date = input("Да/Нет: ").lower()
    if sort_date == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        sort_order = input("По возрастанию/по убыванию: ").lower()
        if sort_order == "по возрастанию":
            filtered_data = sort_by_date(filtered_data, False)
        else:
            filtered_data = sort_by_date(filtered_data)

    for operation in filtered_data:
        if operation.get("date"):
            operation["date"] = get_date(operation["date"])

    print("\nВыводить только рублевые транзакции?")
    rub_only = input("Да/Нет: ").lower()
    if rub_only == "да":
        filtered_data = list(filter_by_currency(filtered_data, "RUB"))

    print("\nОтфильтровать список транзакций по определенному слову в описании?")
    word_filter = input("Да/Нет: ").lower()
    if word_filter == "да":
        search_word = input("Введите слово для поиска: ")
        filtered_data = process_bank_search(filtered_data, search_word)

    print("\nРаспечатываю итоговый список транзакций...")
    if not filtered_data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(filtered_data)}\n")
        for transaction in filtered_data:
            if transaction.get("from"):
                print(
                    f"{transaction['date']} {transaction['description']}\n"
                    f"{transaction['from']} -> {transaction['to']}\n"
                    f"{transaction['operationAmount']['amount']}"
                )
            else:
                print(
                    f"{transaction['date']} {transaction['description']}\n"
                    f"{transaction['to']}\n"
                    f"{transaction['operationAmount']['amount']}"
                )


if __name__ == "__main__":
    main()
