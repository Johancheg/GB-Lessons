 import time
class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        if self.__color == 'red':
            print(f'Карсный свет...')
            time.sleep(7)
            print(f'Оранжевый свет...')
            time.sleep(2)
            print(f'Зеленый свет!')

        else:
            raise ValueError('Не правильный цвет')

test1 = TrafficLight('red')
test1.running()