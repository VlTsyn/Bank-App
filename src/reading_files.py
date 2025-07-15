from pathlib import Path

import pandas as pd


def reading_from_csv(file_path: str | Path) -> list[dict]:
    """Функция для считывания CSV-файлов"""
    df = pd.read_csv(file_path, sep=";").dropna()
    df["id"] = df["id"].astype(int)
    transactions_list = df.to_dict("records")
    return transactions_list


def reading_from_excel(file_path: str | Path) -> list[dict]:
    """Функция для считывания Excel-файлов"""
    df = pd.read_excel(file_path).dropna()
    df["id"] = df["id"].astype(int)
    transactions_list = df.to_dict("records")
    return transactions_list
