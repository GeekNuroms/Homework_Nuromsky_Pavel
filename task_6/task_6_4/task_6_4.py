# (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
# (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
# Также реализовать парсинг данных из файлов — получить отдельно фамилию,
# имя и отчество для пользователей и название каждого хобби:
# преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь).
# Обосновать выбор типа. Подумать, какие могут возникнуть проблемы при парсинге.
# В словаре должны храниться данные, полученные в результате парсинга.

from collections import namedtuple
from pprint import pprint


def my_logging(content: str, filename='log_result.txt'):
    with open(filename, 'a', encoding='utf-8') as log:
        print(content, file=log)#, print(content)


def name_parse(_name: str): #не смог найти описание типа вывода, корректное
    #  -> namedtuple([str, str, str]) - неверно
    _name = _name.split(',')
    if _name and len(_name) == 3:
        surname, name, father_name = _name
        Fname = namedtuple('FullName', 'surname name father_name')
        fname = Fname(surname, name, father_name)
        return fname

def get_hobby(filename: str, position=0) -> tuple:
    with open(filename, 'br') as hobby_file:
        hobby_file.seek(position)
        hobby = hobby_file.readline()
        hobby = hobby.decode(encoding='utf-8').strip()
        if hobby:
            position = hobby_file.tell()
            hobby = tuple(hobby.split(','))
        else:
            hobby = None
    return hobby, position


with open('full_name.log', 'r', encoding='utf-8') as name_file:
    position = 0
    personal_dict = {}
    for line in name_file:
        hobby, position = get_hobby('hobby_list.txt', position)
        fname = name_parse(line.strip())
        personal_dict[line.strip()] = fname, hobby
        my_logging(f'{line.strip()}: {fname} {hobby}')

pprint(personal_dict)
man = personal_dict.popitem()[1]
print(man[0].name,
      man[0].surname,
      man[0].father_name)


