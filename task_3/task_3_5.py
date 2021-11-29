# 5. Реализовать функцию get_jokes(),
# возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг,
# разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?

from random import choice, shuffle

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def make_ultimate_humor(*arg: list) -> str:
    return ' '.join([choice(list_number) for list_number in arg])


def make_uniq_humor(*arg: list) -> str:
    for lst in arg:
        shuffle(lst)
    return ' '.join([lst.pop() for lst in arg if lst])


def get_jokes(humor_count: int, unique_jokes=False, noun_list=nouns, adverb_list=adverbs,
              adjective_list=adjectives) -> None:

    """
    Some descritpion for everyone

    :param humor_count - количество шуток:
    :param noun_list:
    :param adverb_list:
    :param adjective_list:
    :param unique_jokes - флаг, разрешающий или запрещающий повторы слов в шутках:
    :return:
    """
    usable_func = make_uniq_humor if unique_jokes else make_ultimate_humor
    result = [usable_func(noun_list, adverb_list, adjective_list) for _ in range(humor_count) if
              (noun_list and adverb_list and adjective_list)]
    print(result)


get_jokes(10)
get_jokes(6, unique_jokes=True)
