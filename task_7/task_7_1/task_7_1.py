# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
import os
import yaml

with open('../config.yaml', 'r') as config_file:
    config = yaml.load(config_file, Loader=yaml.FullLoader)
local_config = config.get('config').get('task_7_1')

for folder, sub_folder_list in local_config.items():
    for dir in sub_folder_list:
        os.makedirs(os.path.join(folder, dir))