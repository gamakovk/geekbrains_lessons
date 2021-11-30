"""
Задача 2
2. Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
(добавить кавычку до и кавычку после элемента списка, являющегося числом)
и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
Как модифицировать это условие для чисел со знаком?
Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
Главное: дополнить числа до двух разрядов нулём!
"""

info = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
correct_info = []

for i in info:
    if i.replace("+", "").replace("-", "").isdigit():
        if i.isdigit():
            correct_info.append(f"'{int(i):02}'")
        else:
            correct_info.append(f"'{i[0]}{int(i[1:]):02}'")
    else:
        correct_info.append(i)

print(correct_info)
print(" ".join(correct_info))