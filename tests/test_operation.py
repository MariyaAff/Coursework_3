import pytest

from operation import get_filtered_data, get_data, get_last_values, get_formatted_data


def test_get_data():
    data = get_data()
    assert isinstance(data, list)  # Проверка соответствия


def test_get_filtered_data(test_data):
    assert get_filtered_data(test_data[:2]) == [{
        'date': '2019-07-03T18:35:29.512364',
        'description': 'Перевод организации',
        'from': 'MasterCard 7158300734726758',
        'id': 41428829,
        'operationAmount': {'amount': '8221.37',
                            'currency': {'code': 'USD', 'name': 'USD'}},
        'state': 'EXECUTED',
        'to': 'Счет 35383033474447895560'
    }]

    assert get_filtered_data(test_data[:2], filter_empty_from=True) == [{'date': '2019-07-03T18:35:29.512364',
                                                                         'description': 'Перевод организации',
                                                                         'from': 'MasterCard 7158300734726758',
                                                                         'id': 41428829,
                                                                         'operationAmount': {'amount': '8221.37',
                                                                                             'currency': {'code': 'USD',
                                                                                                          'name': 'USD'}},
                                                                         'state': 'EXECUTED',
                                                                         'to': 'Счет 35383033474447895560'}]


def test_get_last_values(test_data):
    data = get_last_values(test_data, 4)
    assert [x["date"] for x in data] == ['2019-08-26T10:50:58.294041', '2019-07-03T18:35:29.512364',
                                         '2019-04-04T23:20:05.206878']


def test_formatted_data(test_data):
    data = get_formatted_data(test_data)
    assert data == ['26.08.2019 Перевод организации\n'
                    'Maestro 1596 83** **** 5 -> Счет **9589\n'
                    '31957.58 руб.',
                    '03.07.2019 Перевод организации\n'
                    'MasterCard 7158 30** **** 6 -> Счет **5560\n'
                    '8221.37 USD',
                    '04.04.2019 Перевод со счета на счет\n'
                    'Счет 1970 86** **** 8 -> Счет **4188\n'
                    '79114.93 USD']
