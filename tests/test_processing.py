import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def list_of_dict():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {},
    ]


def test_filter_by_executed(list_of_dict):
    assert filter_by_state(list_of_dict) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_canceled(list_of_dict):
    assert filter_by_state(list_of_dict, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_state_out():
    assert (
        filter_by_state(
            [
                {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "date": "2018-10-14T08:21:33.419441"},
            ]
        )
        == "Отсутствует статус"
    )


@pytest.mark.parametrize(
    "example, state, executed",
    [
        ([{"id": 41428829, "date": "2019-07-03T18:35:29.512364"}], "", "Отсутствует статус"),
        ([{"id": 41428829, "state": "MARKED", "date": "2019-07-03T18:35:29.512364"}], "", "Отсутствует статус"),
        (
            [{"id": 41428829, "state": "PENDING", "date": "2019-07-03T18:35:29.512364"}],
            "PENDING",
            [{"id": 41428829, "state": "PENDING", "date": "2019-07-03T18:35:29.512364"}],
        ),
        (
            [{"id": 41428829, "state": "FAILURE", "date": "2019-07-03T18:35:29.512364"}],
            "FAILURE",
            [{"id": 41428829, "state": "FAILURE", "date": "2019-07-03T18:35:29.512364"}],
        ),
        ([], "", "Данные отсутствуют"),
        ("", "", "Данные отсутствуют"),
    ],
)
def test_another_state(example, state, executed):
    assert filter_by_state(example, state) == executed


def test_date_by_decrease(list_of_dict):
    assert sort_by_date(list_of_dict) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_date_by_increase(list_of_dict):
    assert sort_by_date(list_of_dict, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_same_dates():
    assert sort_by_date(
        [
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 41428829, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]
    ) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 41428829, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def date_error():
    return "Некорректная дата"


@pytest.mark.parametrize(
    "example",
    [
        [{"id": 41428829, "state": "EXECUTED", "date": ""}],
        [{"id": 939719570, "state": "EXECUTED"}],
        [{"id": 594226727, "state": "CANCELED", "date": "2018-09-25.241689"}],
        [{"id": 615064591, "state": "CANCELED", "date": "2018-1asgfshg3.419441"}],
    ],
)
def test_wrong_date(example, date_error):
    assert sort_by_date(example) == date_error


def test_empty_list():
    assert sort_by_date([]) == "Данные отсутствуют"
