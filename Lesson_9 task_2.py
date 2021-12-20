"""
Задание 2
Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road:
    def __init__(self, length, width):
        self._length = length
        self.width = width

    def get_full_profit(self, wight=25, thickness=5):
        return f"{self._length} M * {self.width} M * {wight} кг * {thickness} см =" \
               f"{(self._length * self.width * wight * thickness) / 1000} Т"


road_1 = Road(5000, 20)
print(road_1.get_full_profit())
