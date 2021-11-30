# Задание 1

"""
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""

# one_minute = 60
# one_hour = 3600
# one_day = 86400
# one_week = 604800

duration = int(input('Укажите продолжительность в секундах: '))
time_slice = [duration // 86400, duration // 3600 % 24, duration // 60 % 60, duration % 60]
print('duration = ', duration)
print(time_slice[0], 'день', time_slice[1], 'час', time_slice[2], 'мин', time_slice[3], 'сек')