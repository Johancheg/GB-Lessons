def thesaurus(*names):
    dict_names = {}
    for name in names:
        key = name[0].title()
        if key not in dict_names:
            dict_names[key] = []
        dict_names[key].append(name)
    return dict_names



print(thesaurus('Илья Антонов','Антон', 'Alex', 'Debby', 'Henry', 'Jerry', 'Jennifer'))