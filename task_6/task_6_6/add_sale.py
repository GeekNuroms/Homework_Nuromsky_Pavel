from sys import argv
# from os import listdir


def my_logging(content: str, filename=argv[0].replace('add_sale.py', 'bakery.csv')):
    with open(filename, 'a', encoding='utf-8') as log:
        print(content, file=log)


value = argv[1] if len(argv) > 1 else '12376'

if value.replace('.', '').isdigit():
    my_logging(value)
else:
    print('Недопустимое значение')
