# Задание №3


"""

Склонение слова
Реализовать склонение слова «процент» во фразе «N процентов».
Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов
"""

for i in range(100):
    new_str = str(i+1)
    new_list = list(new_str)
    if int(new_list[-1]) == 1 and i+1 != 11:
        # print(f"{i + 1} процент")
        print(i + 1, "процент")
    elif 1 < int(new_list[-1]) <= 4:
        if 10 < i + 1 <= 14:
            # print(f"{i + 1} процентов")
            print(i + 1, "процентов")
        else:
            # print(f"{i + 1} процента")
            print(i + 1, "процента")
    else:
        # print(f"{i + 1} процентов")
        print(i + 1, "процентов")