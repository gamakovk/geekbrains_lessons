"""
Задание 4
Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
Убедиться, что ничего лишнего не происходит.
"""

from requests import get, utils

response = utils.get_unicode_from_response(get("https://www.cbr.ru/scripts/XML_daily.asp"))


def currency_rates(code):
    content = response.split("Valute ID=")
    for i in content:
        if code.upper() in i:
            print(code.upper(), end=" ")
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))


if __name__ == "__main__":
    print(currency_rates("USD"))
    print(currency_rates("EUR"))

import utils

print(utils.currency_rates("CNY"))
