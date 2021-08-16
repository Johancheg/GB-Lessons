import requests
from decimal import *

def currency_rates(val):
    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    char_dict = {}
    val = val.upper()
    if len(val) == 3 and r.find(val) != -1:
        key = r.find(val.upper())
        res = r[key:(key + 3)]
        v1 = r.find('Value', key)
        v2 = r.find('/Value', key)
        r = r[(v1 + 6):(v2 - 1)]
        r = Decimal(r.replace(',','.')).quantize(Decimal('1.11'))
        char_dict.setdefault(res, r)
    else:
        return print(f'None')
    return print(f'{char_dict[val]}')
currency_rates('usd')