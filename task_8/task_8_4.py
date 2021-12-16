# 4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции
# и выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
# Примечание: сможете ли вы замаскировать работу декоратора?

def int_validator(*args) -> list:
    return [value for value in args if not isinstance(value, int)]

# print(int_validator(67, 77, 6, '5656'))

def cubometer(*args):
    return [val ** 3 for val in args]


def data_checker(func=cubometer, validator=int_validator):
    def upper_decorator(_func):
        def wrapped(*args):
            wrong_list = validator(*args)
            if wrong_list:
                raise ValueError(f'Некорректные данные {wrong_list}')
            return func(*args)
        return wrapped
    return upper_decorator


print(cubometer(2, 4, 5))


@data_checker(validator=int_validator)
def cubometer(*args):
    return [val ** 3 for val in args]

print(cubometer(2, 4, 5))
print(cubometer(2, 4, 5, '5', 'gggg'))