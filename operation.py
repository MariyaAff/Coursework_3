import json
from datetime import datetime

"""Функция чтения json-файла"""


def get_data():
    with open('operations.json', encoding='utf-8') as file:
        data = json.load(file)  # Возвращает список
    return data


"""Функция обработки данных"""


def get_filtered_data(data, filter_empty_from=False):
    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]  # Синтаксический сахар: цикл по полученному списку
    if filter_empty_from:
        data = [x for x in data if "from" in x]  # Синтаксический сахар: цикл по полученному списку
    return data  # Возвращает отфильтрованные данные


"""Функция сортировки по дате"""


def get_last_values(data, count_last_values):
    data = sorted(data, key=lambda x: x["date"], reverse=True)  # Сортировка даты в обратном порядке
    data = data[:count_last_values]  # Последние 5 дат
    return data  # Вернет отсортированный список


"""Функция форматирования даты, номеров карт отправителя и получателя"""


def get_formatted_data(data):
    formatted_data = []
    for row in data:
        date = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")  # Использование метода получения даты из строки, затем получение даты заданного вида
        description = row["description"]
        recipient = f"{row['to'].split()[0]} **{row['to'][-4:]}"  # Получатель: вытащит первое слово целиком, номер счета отформатирован
        operations_amount = f"{row['operationAmount']['amount']} {row['operationAmount']['currency']['name']}"  # Число и валюта
        if "from" in row:  # Если есть отправитель
            sender = row["from"].split()  # Получить список
            from_bill = sender.pop(-1) # Вытащить последнее значение и удалит из списка
            from_bill = f"{from_bill[:4]} {from_bill[4:6]}** **** {from_bill[-4]}"  # Замена номера счета на *
            from_info = " ".join(sender)
        else:
            from_info, from_bill = "", ""
        formatted_data.append(f"""\
{date} {description}
{from_info} {from_bill} -> {recipient}
{operations_amount}""")
    return formatted_data
        

