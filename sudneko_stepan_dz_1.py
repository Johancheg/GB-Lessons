def num_translate(numb):
    numb_dict = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'for': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'

    }
    for key, val in numb_dict.items():
        if numb == key:
            return val

print(num_translate('eleewen'))