# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

import os
import django


def mod_size(i):
    """https://stackoverflow.com/questions/2189800/how-to-find-length-of-digits-in-an-integer"""
    return 10**len("%i" % i)


size_dict = {10**i: 0 for i in range(1, 8)}
root_dir = django.__path__[0]
for root, dirs, local_files in os.walk(root_dir):
    if local_files:
        for file in local_files:
            path = os.path.join(root, file)
            size = mod_size(os.stat(path).st_size)
            size_dict[size] += 1
print(size_dict)


