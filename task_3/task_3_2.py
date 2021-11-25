# 2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы —
# результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

translate_dict = {'zero': 'ноль',
                  'one': 'один',
                  'two': 'два',
                  'three': 'три',
                  'four': 'четыре',
                  'five': 'пять',
                  'six': 'шесть',
                  'seven': 'семь',
                  'eight': 'восемь',
                  'nine': 'девять'
                  }


def num_translate_adv(number: str, _dict=translate_dict) -> str or None:
    number_mod = f'{number[0].lower()}{number[1:]}'
    result = _dict.get(number_mod)
    if not result:
        return
    elif number[0].isupper():
        return result.capitalize()
    return result


print(num_translate_adv('One'),
      num_translate_adv('two'),
      num_translate_adv('tWo'),
      num_translate_adv('test'))
