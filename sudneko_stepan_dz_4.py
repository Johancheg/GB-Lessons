class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} стартанула'
    def stop(self):
        return f'{self.name} остановилась'
    def turn(self, direction):
        return f'Машина {self.name} повернула {direction}'
    def show_speed(self):
        return f'Текущая скорость автомобиля: {self.speed} '

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Первыешение скорости! Снизьте скорость!')


class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Первыешение скорости! Снизьте скорость!')

class PolicCar(Car):
    pass