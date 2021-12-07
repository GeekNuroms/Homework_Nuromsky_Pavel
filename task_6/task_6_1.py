# 1. Не используя библиотеки для парсинга, распарсить
# (получить определённые данные) файл логов web-сервера nginx_logs.txt
# получить список кортежей вида:
# (<remote_addr>, <request_type>, <requested_resource>). Например:
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера

from pprint import pprint


def string_parser(raw_string: str) -> tuple:
    parse_result = (raw_string.split())
    return parse_result[0], parse_result[5].strip('"'), parse_result[6]


def my_logging(content: str, filename='log.log'):
    with open(filename, 'a', encoding='utf-8') as log:
        print(content, file=log)#, print(content)


log_list = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as file: #можно заменить на 'micro_log.txt'
    for line in file:
        one_string = string_parser(line)
        log_list.append(one_string)
        # my_logging(one_string) #логирование в файл

pprint(log_list)