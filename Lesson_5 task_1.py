"""
Задание 1
1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
#  >>> odd_to_15 = odd_nums(15)
#  >>> next(odd_to_15)
1
#  >>> next(odd_to_15)
3
...
#  >>> next(odd_to_15)
15
#  >>> next(odd_to_15)
...StopIteration...
"""

num = int(input('Ввдите число: '))


def odd_nums(nums):
    for n in range(1, nums + 1, 2):
        yield n


for i in odd_nums(num):
    print(i)
