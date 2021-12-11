"""
Задание 1
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список
 кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]
Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""

with open("parse_logs.txt", "w", encoding="utf-8") as p:
    with open("nginx_logs.txt", "r", encoding="utf-8") as f:
        content = ((line.split()[0], line.split()[5], line.split()[6]) for line in f)
        for i in content:
            print(i, file=p)
