def num_translate_adv(numb): ##### не самый лучший способ, как оказалось после разбора
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
    numb_dict2 = {
        'Zero': 'Ноль',
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'For': 'Четыре',
        'Five': 'Пять',
        'Six': 'Шесть',
        'Seven': 'Семь',
        'Eight': 'Восемь',
        'Nine': 'Девять',
        'Ten': 'Десять'

    }
    for key, val in numb_dict.items():
        if numb == key:
            return val
        else:
            for key, val in numb_dict2.items():
                if numb == key:
                    return val

print(num_translate_adv('One'))