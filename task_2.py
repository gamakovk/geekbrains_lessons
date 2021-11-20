# Задание 2

"""
Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
сумма цифр которых делится нацело на 7.
* Решить задачу под пунктом b, не создавая новый список.
"""

# check sum
# 17485588610
# 15392909930


list_of_cubes = []
add_list_of_cubes = []
all_sum = 0

for i in range(1, 1000, 2):
    list_of_cubes.append(i ** 3)
for ind, val in enumerate(list_of_cubes):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        all_sum += list_of_cubes[ind]
print(all_sum)

for m in list_of_cubes:
    add_list_of_cubes.append(m + 17)
all_sum = 0
for ind, val in enumerate(add_list_of_cubes):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        all_sum += add_list_of_cubes[ind]
print(all_sum)
