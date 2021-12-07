# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных
# им запросов по данным файла логов из предыдущего задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов;
# код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

from pprint import pprint
# from collections import Counter


def dict_factory(raw_string: str, exec_dict: dict) -> dict:
    parse_result = (raw_string.split())
    exec_dict.setdefault(parse_result[0], 0)
    exec_dict[parse_result[0]] += 1
    return exec_dict


def my_logging(content: str, filename='log.log'):
    with open(filename, 'a', encoding='utf-8') as log:
        print(content, file=log)#, print(content)


def find_hooligan(input_dict: dict, count_num=5) -> list:
    sorted_tuple = sorted(input_dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_tuple[:count_num + 1]


spam_dict = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    for line in file:
        dict_factory(line, spam_dict)
        # my_logging(dict_factory) #логирование в файл

pprint(spam_dict)
hooligans = find_hooligan(spam_dict, 15)
pprint(hooligans)
