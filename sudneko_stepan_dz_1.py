import re
EMAIL = re.compile(r"([a-z0-9]+)@([a-z0-9]+\.[a-z]+)")
def email_parse(adress):
    log_domain = EMAIL.findall(adress)[0]
    my_dict = {'username': None,
               'domain': None}
    if log_domain:
        log, domain = log_domain
        my_dict.update({'username': log, 'domain': domain})

    else:
        raise ValueError(f'Неправильный адресс {adress}')
    print(my_dict)

email_parse('123mile@3213lolo.net')