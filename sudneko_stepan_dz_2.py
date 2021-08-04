data = []
for i in range(1,1001):
    if not i % 2 ==0:
        data.append(i ** 3)
print(data)

sum_of_numbers1 = 0
for indx in range(len(data)):
    new = 0
    f = str(data[indx])
    for i in f:
        new += int(i)
        if new % 7 == 0:
            sum_of_numbers1 += (data[indx])
print(sum_of_numbers1)

sum_of_numbers2 = 0
for indx in range(len(data)):
    new = 0
    f = str(data[indx] + 17)
    for i in f:
        new += int(i)
        if new % 7 == 0:
            sum_of_numbers2 += (data[indx])
print(sum_of_numbers2)