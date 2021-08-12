numbers = [57.8, 46.51, 97, 88, 55, 22.1, 33.8, 256, 214.155, 10000, 1200]
for numb in numbers:
    r = int(numb)
    k = (numb - r) * 100
    print(f'{r} руб {k:02.0f} коп')



numbers = [57.8, 46.51, 97, 88, 55, 22.1, 33.8, 256, 214.155, 10000, 1200]
print(id(numbers))
numbers.sort()
print(id(numbers))
for numb in numbers:
    r = int(numb)
    k = (numb - r) * 100
    print(f'{r} руб {k:02.0f} коп')


numbers = [57.8, 46.51, 97, 88, 55, 22.1, 33.8, 256.55, 214.155, 10000, 1200]
for numb in sorted(numbers)[::-1][:5]:
    r = int(numb)
    k = (numb - r) * 100
    print(f'{r} руб {k:02.0f} коп')


print([f'{int(numb)} руб {(numb - int(numb)) * 100:02.0f} коп' for numb in sorted(numbers)[::-1][:5]])