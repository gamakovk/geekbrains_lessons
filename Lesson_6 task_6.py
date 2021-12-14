"""
Задание 6
Реализовать простую систему хранения данных о суммах продаж булочной.
Должно быть два скрипта с интерфейсом командной строки: для записи данных и для вывода на экран записанных данных.
При записи передавать из командной строки значение суммы продаж.
Для чтения данных реализовать в командной строке следующую логику:
просто запуск скрипта — выводить все записи;
запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу,
по номер, равный второму числу, включительно.
Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1. Примеры запуска скриптов:

python add_sale.py 5978,5
python add_sale.py 8914,3
python add_sale.py 7879,1
python add_sale.py 1573,7
python show_sales.py
5978,5
8914,3
7879,1
1573,7
python show_sales.py 3
7879,1
1573,7
python show_sales.py 1 3
5978,5
8914,3
7879,1
"""

# Show sales
from sys import argv

with open("bakery.csv", "r", encoding="utf-8") as donut_r:
    if 1 < len(argv) < 4 and [i for i in argv[1:] if i.isdigit()]:
        if len(argv) == 3:
            start, finish = map(int, argv[1:])
            print(*(v for i, v in enumerate(donut_r) if start - 1 <= i <finish), sep="")
        else:
            print(*(v for i, v in enumerate(donut_r) if i >= int(argv[1]) - 1), sep="")
    else:
        print(donut_r.read())

#  Add sales
from sys import argv

with open("bakery.csv", "a", encoding="utf-8") as donut_a:
    with open("bakery.csv", "r", encoding="utf-8") as donut_r:
        if len(argv) > 1 and [i for i in argv[1:] if "." in i and i.replace(".", "").isdigit()]:
            if round(float(argv[1]), 3) <= 99999.999:
                print(f'{round(float(argv[1]), 3):>010}', file=donut_a)
            else:
                print("Number must be less than 99 999,999")
        else:
            print(donut_r.read())
