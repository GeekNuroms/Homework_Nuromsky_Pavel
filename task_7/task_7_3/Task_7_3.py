# 3. Создать структуру файлов и папок, как написано в задании
# 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html

import os
from collections import defaultdict
from pprint import pprint
import shutil

root_dir = r'..\task_7_2\my_project'
new_placement = r'.\templates'

if not os.path.exists(new_placement):
    os.makedirs(new_placement)


for root, dirs, files in os.walk(root_dir):
    val = root.rsplit('\\')
    if root.rsplit('\\')[-1] == 'templates':
        for folder in dirs:
            try:
                from_path = os.path.join(root, folder)
                new_path = os.path.join(new_placement, folder)
                shutil.copytree(from_path, new_path)
            except FileExistsError as err:
                print(f'Из {folder} все уже украдено до нас' )

