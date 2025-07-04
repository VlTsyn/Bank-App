import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
URL = os.getenv("URL")


def transaction_converter(transaction: dict) -> float:
    """Функция конвертации USD и EUR в рубли"""
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    elif transaction["operationAmount"]["currency"]["code"] == "USD":
        url = f"{URL}?to=RUB&from=USD&amount={transaction["operationAmount"]['amount']}"
        payload = {}
        headers = {"apikey": API_KEY}

        response = requests.request("GET", url, headers=headers, data=payload)

        result = response.json()

        return result["result"]
    elif transaction["operationAmount"]["currency"]["code"] == "EUR":
        url = f"{URL}?to=RUB&from=EUR&amount={transaction["operationAmount"]['amount']}"
        payload = {}
        headers = {"apikey": API_KEY}

        response = requests.request("GET", url, headers=headers, data=payload)

        result = response.json()

        return result["result"]
