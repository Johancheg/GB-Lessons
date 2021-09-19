class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) \
               + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return str(self.nums)

    def __add__(self, other):
        return 'Сумма клеток равна ' + str(self.nums + other.nums)
        # return Cell(self.nums + other.nums)

    def __sub__(self, other):
        return self.nums - other.nums if self.nums - other.nums > 0 \
            else 'Клетка не может быть меньше нуля!'

    def __mul__(self, other):
        return 'Умножение клеток равно  ' + str(self.nums * other.nums)

    def __truediv__(self, other):
        return 'Деление клеток равно ' + str(round(self.nums / other.nums))


cell_1 = Cell(10)
cell_2 = Cell(34)
print(cell_1)
print(cell_1 - cell_2)
print(cell_2.make_order(10))