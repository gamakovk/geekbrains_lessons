"""
Задание 1
Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает
 имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден,
 выбросить исключение ValueError. Пример:
#  >>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
#  >>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
имеет ли смысл в данном случае использовать функцию re.compile()?
"""

import re


def email_parse(email_address):
    re_email = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not re_email.match(email_address):
        raise ValueError(f'wrong email: {email_address}')
    print(re_email.match(email_address).groupdict())

for i in ['someone@geekbrains.ru', 'som&eone@geekbrainsru', 'someone@geekbrainsru']:
    try:
        email_parse(i)
    except ValueError as err:
        print(err)
