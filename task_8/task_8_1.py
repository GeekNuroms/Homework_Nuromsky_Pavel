# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает
# имя пользователя и почтовый домен из email адреса и
# возвращает их в виде словаря. Если адрес не валиден,
# выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?

import re

input = ['so@meone@geekbrains.ru', 'someone@geekbrains.ru', 'ffsfd@yandex.ru', 'kjkjhh', 'ru@ru', 'turu@.ru', 'fsdf@tu.tu']


def email_parse(input_list: list) -> dict:
    pattern = re.compile(r'@')
    domain_validation = re.compile(r'\S+\.[\w,\.,\d]{2,}$')
    user_validation = re.compile(r'^[\w,\d]+$')
    out_dict = {}
    for text in input_list:
        try:
            basic_split = ('regex.split:', pattern.split(text))
            if len(basic_split[1]) != 2:
                raise ValueError
            user, domain = basic_split[1]
            valid_user = re.fullmatch(user_validation, user)
            valid_domain = re.fullmatch(domain_validation, domain)
            if not (valid_user and valid_domain):
                raise ValueError
            else:
                 out_dict[user] = domain
        except ValueError as err:
            print(err)
    return out_dict


print(email_parse(input))
