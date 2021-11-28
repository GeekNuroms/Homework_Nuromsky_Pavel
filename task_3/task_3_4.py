# 4. * (вместо задачи 3) Написать функцию thesaurus_adv(),
# принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь,
# в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего задания
# и содержащие записи, в которых фамилия начинается с соответствующей буквы.
# Например:
# >>>thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }


def thesaurus_adv(*args: str) -> dict:
    person_dict = {}
    for full_name in args:
        name, surname = full_name.split(' ')
        inner_dict = person_dict.get(surname[0])
        if not inner_dict:  # Нет букв фамилии
            person_dict[surname[0]] = {name[0]: [full_name, ]}
        elif name[0] not in inner_dict:
            inner_dict[name[0]] = [full_name, ]
        else:
            inner_dict[name[0]].append(full_name)
    print(f"\n{'-'*150}\n{args}\n{'-'*150}\n{person_dict}\n{'-'*150}")
    return person_dict


def sorted_dict_by_key(input_dict: dict) -> dict:
    sorted_tuple = sorted(input_dict.items(), key=lambda item: item[0])
    _sorted_dict = {key: value for key, value in sorted_tuple}
    return _sorted_dict


out_dict = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
sorted_dict = sorted_dict_by_key(out_dict)
s2_dict = {key: sorted_dict_by_key(value) for key, value in sorted_dict.items()}
print(f"\n{'-'*150}\nИсходный словарь\n{out_dict}\n{'-'*150}\nСортировка по ключу\n{sorted_dict}\n{'-'*150}")
print(f"{'-'*150}\nСортировка по ключу, уровень имен\n{s2_dict}\n{'-'*150}")











