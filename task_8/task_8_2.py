# 2. * (вместо 1) Написать регулярное выражение для парсинга файла логов
# web-сервера из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# для получения информации вида:
# (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>),
# например:
#
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле?
# Были ли особенные строки? Можно ли для них уточнить регулярное выражение?

import re


template = re.compile(r'\s{2}|\"|\s\-\s\-\s|\s/')

log_list = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    for line in file:
        one_string = template.split(line)
        record = one_string[0], re.sub(r'\[|\]', '', one_string[1]).strip(), one_string[2],\
                 one_string[3], one_string[4].split()[0], one_string[4].split()[1]
        log_list.append(record)
for s in log_list:
    print(s)
