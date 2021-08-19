num = int(input('Введите крайнее число для генератора: '))
nums_gen = (num for num in range(1, num + 1, 2))
print(*nums_gen)
print((type(nums_gen)))