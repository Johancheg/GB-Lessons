class Worker:
    my_dict = {
        'wage': 20000,
        'bonus': 15000
    }
    def __init__(self, name, surname, position):

        self.name = name
        self.surname = surname
        self.position = position
        self._income = self.my_dict['wage'], self.my_dict['bonus']

class Position(Worker):
    def get_full_name(self):
        return print(f'Фамилия:{self.surname} Имя:{self.name}')
    def get_total_income(self):
        return print(f'Оклад и бонус: {self._income}')

Position('St', 'TS', 'Cheif').get_full_name()
Position('St', 'TS', 'Cheif').get_total_income()