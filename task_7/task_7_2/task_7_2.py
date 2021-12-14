# 2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html

from pprint import pprint
import os
from shutil import rmtree
import yaml
from collections import defaultdict


# pprint(local_config)


def my_logging(content: str, filename='log_result.log'):
    with open(filename, 'w', encoding='utf-8') as log:
        print(content, file=log)#, print(content)


def dict_to_file_struct(input_dict: dict):
    all_path_list = [input_dict, ]
    while all_path_list:
        next_dict = all_path_list.pop()
        for mother_path, file_or_dict_list in next_dict.items():
            for file_or_dict in file_or_dict_list:
                pprint(file_or_dict)
                if isinstance(file_or_dict, dict):
                    for new_dir in file_or_dict.keys():
                        new_dir_path = os.path.join(mother_path, new_dir)
                        all_path_list.append({new_dir_path: file_or_dict.get(new_dir)})
                        os.makedirs(new_dir_path)
                else:
                    new_file = os.path.join(mother_path, file_or_dict)
                    my_logging(content='some text', filename=new_file)


with open('../config.yaml', 'r') as config_file:
    config = yaml.load(config_file, Loader=yaml.FullLoader)
local_config = config.get('config').get('task_7_2')
dict_to_file_struct(local_config)













# for folder, sub_folder_list in local_config.items():
#     for dir in sub_folder_list:
#         os.makedirs(os.path.join(folder, dir))