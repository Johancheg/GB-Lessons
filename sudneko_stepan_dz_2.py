class Road:
    def __init__(self, length, width):
        self.__road_len = int(length)
        self.__road_len_width = int(width)

    def road_calculate(self):
        weight = 25
        thickness = 5
        result = (self.__road_len * self.__road_len_width * weight * thickness) * 0.001
        return int(result)

road1 = Road(20,5000)
print(road1.road_calculate())