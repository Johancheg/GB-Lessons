import requests
from datetime import datetime
from decimal import *


def currency_rates(val):
    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    date = r.find('date')
    char_dict = {}
    val = val.upper()
    d = r.find('Date')
    date1 = r[(d + 6):(d + 16)]
    current_date = datetime.strptime(date1, '%d.%m.%Y').date()
    if len(val) == 3 and r.find(val) != -1:
        key = r.find(val.upper())
        res = r[key:(key + 3)]
        v1 = r.find('Value', key)
        v2 = r.find('/Value', key)
        r = r[(v1 + 6):(v2 - 1)]
        r = Decimal(r.replace(',','.')).quantize(Decimal('1.11'))
        char_dict.setdefault(res, r)
        return print(f'{char_dict[val]}, {current_date}')
    else:
        return print(f'None')



if __name__ == '__main__':
    currency_rates('TT')