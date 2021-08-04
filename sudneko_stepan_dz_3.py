persent_var1 = 'процент'
persent_var2 = 'процента'
persent_var3 = 'процентов'

for x in range(1, 101):
    y = x % 10
    if y == 1 and not(11 <= x <= 14):
        print(x, persent_var1)
    elif 2 <= y <= 4 and not(11 <= x <= 14):
        print(x, persent_var2)
    elif 5 <= y <= 9 or y == 0 or (11<= x <= 14):
        print(x, persent_var3)