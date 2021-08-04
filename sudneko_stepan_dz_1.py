# Кол-во сек. задается пользователем
duration = int(input('Введите кол-во секунд: '))
day = duration//86400
hour =  (duration - (day * 86400)) // 3600
minute = (duration - ((day * 86400) + (hour * 3600))) // 60
seconds = (duration - ((day * 86400) + (hour * 3600) + (minute * 60)))
if duration < 60:
    print(seconds, 'сек')
elif duration > 60 and duration < 3600:
    print(minute, 'мин', seconds, 'сек')
elif duration > 3600 and duration < 86400:
    print(hour, 'час', minute, 'мин', seconds, 'сек')
else:
    print(day,'дн', hour, 'час', minute, 'мин', seconds, 'сек')


# Заранее заданное кол-во
duration = 87000
day = duration//86400
hour =  (duration - (day * 86400)) // 3600
minute = (duration - ((day * 86400) + (hour * 3600))) // 60
seconds = (duration - ((day * 86400) + (hour * 3600) + (minute * 60)))
if duration < 60:
    print(seconds, 'сек')
elif duration > 60 and duration < 3600:
    print(minute, 'мин', seconds, 'сек')
elif duration > 3600 and duration < 86400:
    print(hour, 'час', minute, 'мин', seconds, 'сек')
else:
    print(day,'дн', hour, 'час', minute, 'мин', seconds, 'сек')