src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
res = [src[i] for i in range(len(src)) if src.count(i) == src.count(1)]
print(res)
