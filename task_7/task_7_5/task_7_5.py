# 5. * (вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи те же, а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
#   {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.

import os
import django
import json

def mod_size(i):
    return 10**len("%i" % i)


size_dict = {10**i: [0 , set()] for i in range(1, 8)}
root_dir = django.__path__[0]
for root, dirs, local_files in os.walk(root_dir):
    if local_files:
        for file in local_files:
            path = os.path.join(root, file)
            size = mod_size(os.stat(path).st_size)
            size_dict[size][0] += 1
            size_dict[size][1].add(file.rsplit('.')[-1])
print(size_dict)
size_dict = {key: (val[0], list(val[1])) for key, val in size_dict.items()}
print(size_dict)#зачем так непонятно
