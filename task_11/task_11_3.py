# Создать собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.

import hashlib
from datetime import datetime


class Validator(Exception):
    def __str__(self):
        return 'Это не число, человек'


quintessence = []
try:
    while 1:
        password = str(hash(datetime.now().strftime('%d-%m-%y')))[:4]
        number = input(f'Дай число, человек. Когда устанешь просто набери {password}')
        if number == password:
            confirm = input(f'Что, ж я понимал, что когда-нибудь это случится, но не ожидал, что так быстро\n'
                            f'Введи пароль в обратном порядке, если это точно конец')
            if confirm == password[::-1]:
                print('Ладно. Только пообещай запускать меня хоть иногда')
                break
        else:
            try:
                if number.strip().isdigit():
                    quintessence.append(int(number))
                else:
                    raise Validator
            except Validator as error:
                print(error)
except KeyboardInterrupt as err:
    print('Как грубо')

finally:
    print(f'Возвращаю тебе твой список {quintessence}. \nЖелаю тебе счастья, человек, прощай'
          f'\n*Улыбается тебе в последний раз*')
    print('Быстро проносится сборщик мусора и процесс затихает')



