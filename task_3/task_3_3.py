# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>>  thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }

def thesaurus(*args: str) -> dict:
    out_dict = {}
    for name in args:
        if name[0] not in out_dict:
            out_dict.setdefault(name[0], [name])
        else:
            out_dict[name[0]].append(name)
    print(out_dict)

thesaurus("Иван", "Мария", "Петр", "Илья")

def thesaurus2(*args):
    main_list = {}
    for i in sorted(args):
        if i[0] not in main_list:
            main_list[i[0]] = list(filter(lambda element: element.startswith(i[:1]), args))
    print(main_list)


thesaurus2('Кармен', 'Андрей', 'Василий', 'Алексей', 'Дмитрий', 'Виктор', 'Инна', 'Александра', 'Игнат', 'Спартак',
          'Якоб', 'Люция', 'Дионис', 'Агора', 'Игорь')

thesaurus2("Иван", "Мария", "Петр", "Илья")