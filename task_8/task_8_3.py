# 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
# можете ли вы вывести тип значения функции?
# Сможете ли решить задачу для именованных аргументов?
# Сможете ли вы замаскировать работу декоратора?
# Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

from functools import wraps


def logthis(a_function_to_decorate):
    @wraps(a_function_to_decorate)
    def wrapped(*args, **kwargs):
        for val in args:
            print(val, type(val))
        a_function_to_decorate(*args, **kwargs)
        print(f'{a_function_to_decorate.__name__} was logged')  # print or log results after the func is executed
        return
    return wrapped


def cubometer(*args):
    return [val ** 3 for val in args]


print(cubometer(2, 4, 5))


@logthis
def cubometer(*args):
    return [val ** 3 for val in args]


cubometer(2, 4, 5)
