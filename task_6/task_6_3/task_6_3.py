# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип:
# одна строка — один пользователь, разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
# ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
# Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.

from pprint import pprint


def my_logging(content: str, filename='log_result.log'):
    with open(filename, 'a', encoding='utf-8') as log:
        print(content, file=log)#, print(content)


def get_hobby(filename: str, position=0) -> tuple:
    with open(filename, 'br') as hobby_file:
        hobby_file.seek(position)
        hobby = hobby_file.readline()
        hobby = hobby.decode(encoding='utf-8')
        if hobby:
            position = hobby_file.tell()
        else:
            hobby = None
    return hobby, position


with open('full_name.log', 'r', encoding='utf-8') as name_file:
    position = 0
    personal_dict = {}
    for name in name_file:
        hobby, position = get_hobby('hobby_list.txt', position)
        if isinstance(hobby, str):
            hobby = hobby.strip()
        personal_dict[name.strip()] = hobby
        my_logging(f'{name.strip()}: {hobby}')

pprint(personal_dict)


