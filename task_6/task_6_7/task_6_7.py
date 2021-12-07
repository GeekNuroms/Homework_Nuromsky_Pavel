# 7. * (вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта:
# передаём ему номер записи и новое значение. При этом файл не должен читаться целиком — обязательное требование.
# Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не существует.


from sys import argv
from collections import deque
import os


def input_validation(input_list: list):
    if len(input_list) == 2 and input_list[0].isdigit():
        input_list[0] = int(input_list[0])
        return True, tuple(input_list)
    return False, []


def edit_file(input_values: tuple):
    filename = argv[0].replace('task_6_7.py', 'bakery.csv')
    filename2 = argv[0].replace('task_6_7.py', 'temp.csv')
    record, text = input_values
    with open(filename, 'r', encoding='utf-8') as file, open(filename2, 'a', encoding='utf-8') as new_file:
        str_count = 0
        for line in file:
            str_count += 1
            if record == str_count:
                line = f'{text}\n'
            new_file.write(line)
    if str_count < record:
        print('Нет такой строки')
    else:
        os.system(f' copy {filename2} {filename}')
        os.remove(filename2)
        # os.system(' cp src.txt targ.txt')
        print(f'Небывалый успех в редактировании {filename}')


result, input_list = input_validation(argv[1:])
if not result:
    print('Некорректные данные')
else:
    edit_file(input_list)
