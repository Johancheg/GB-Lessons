from itertools import zip_longest
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Елена', 'Антон', 'Павел'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
res1 = (res for res in zip_longest(tutors, klasses[:len((tutors))], fillvalue='None'))
print(*res1)
print(type(res1))