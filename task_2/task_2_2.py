# 2. Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем)
# кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом)
# и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
#
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
#
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
# Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
# Главное: дополнить числа до двух разрядов нулём!

###Не заморачиваясь с ковычками
marker_symbols = ['+', '-']
input_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
out_list = []
for value in input_list:
    symbol = ''
    if value[0] in marker_symbols:
        symbol, value = value[0], value[1:]
    if value.isdigit():
        if -10 < int(value) < 10:
            out_list.append(f'"{symbol}0{value}"')
        else:
            out_list.append(f'"{symbol}{value}"')
    else:
        out_list.append((f'{symbol}{value}'))
print(' '.join(out_list))