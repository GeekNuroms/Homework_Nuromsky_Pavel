from sys import argv
# from collections import deque


def input_validation(input_list: list):
    if input_list:
        number_list = [int(number) for number in input_list[:2] if number.isdigit()]
        if len(number_list) == 1:
            number_list.append(0)
        return number_list


def read_file(val):
    filename = argv[0].replace('show_sales.py', 'bakery.csv')
    value_list = input_validation(val)
    with open(filename, 'r', encoding='utf-8') as file:
        if not value_list:
            for line in file:
                print(line)
            return
        else:
            string_num = 0
            begin, end = value_list
            for line in file:
                string_num += 1
                if begin - 1 < string_num:
                    print(line)
                    if end and string_num == end:
                        break


value = argv[1:]
print(value)
print('_'*100)
read_file(value)
