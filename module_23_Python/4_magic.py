"""
Задача 4. Магия
Для одной игры необходимо реализовать механику магии,
где при соединении двух элементов получается новый.
У нас есть четыре базовых элемента: «Вода», «Воздух», «Огонь», «Земля».
Из них получаются новые: «Шторм», «Пар», «Грязь», «Молния», «Пыль», «Лава».

Таблица преобразований:
Вода + Воздух = Шторм;
Вода + Огонь = Пар;
Вода + Земля = Грязь;
Воздух + Огонь = Молния;
Воздух + Земля = Пыль;
Огонь + Земля = Лава.
Напишите программу, которая реализует все эти элементы.
Каждый элемент необходимо организовать как отдельный класс.
Если результат не определён, то возвращается None.

Примечание: сложение объектов можно реализовывать через магический метод __add__,
вот пример использования:

class ExampleOne:

    def __add__(self, other):
        return ExampleTwo()

class ExampleTwo:
    answer = 'сложили два класса и вывели'
first_example = ExampleOne()
second_example = ExampleTwo()
result = first_example + second_example
print(result.answer)

Дополнительно: придумайте свой элемент (или элементы)
и реализуйте его взаимодействие с остальными.
"""


class Water:

    def __str__(self):
        return 'Water'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        if isinstance(other, Fire):
            return Steam()
        if isinstance(other, Earth):
            return Dirt()
        return None



class Air:
    def __str__(self):
        return 'Air'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        if isinstance(other, Earth):
            return Dust()
        if isinstance(other, Water):
            return Storm()
        return None


class Fire:
    def __str__(self):
        return 'Fire'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        if isinstance(other, Water):
            return Steam()
        if isinstance(other, Air):
            return Lightning()
        return None


class Earth:
    def __str__(self):
        return 'Earth'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        if isinstance(other, Air):
            return Dust()
        if isinstance(other, Fire):
            return Lava()
        return None


class Storm:
    def __str__(self):
        return 'Storm'


class Steam:
    def __str__(self):
        return 'Steam'


class Dirt:
    def __str__(self):
        return 'Dirt'


class Lightning:
    def __str__(self):
        return 'Lightning'


class Dust:
    def __str__(self):
        return 'Dust'


class Lava:
    def __str__(self):
        return 'Lava'


water_elem = Water()
air_elem = Air()
fire_elem = Fire()
earth_elem = Earth()

base_elems = [water_elem, air_elem, fire_elem, earth_elem]
new_elems = list()


for i, elem_1 in enumerate(base_elems):     # use enumerate to get counter i
    for elem_2 in base_elems[i + 1::]:      # to avoid get twice the same pair
        new_elem = elem_1 + elem_2
        new_elems.append(new_elem)
        print(f'Mix {elem_1} and {elem_2} you get {new_elem}')


# print(new_elems)


# storm_elem = water_elem + air_elem
# print(storm_elem)
#
# steam_elem = water_elem + fire_elem
# print(steam_elem)
#
# dirt_elem = water_elem + earth_elem
# print(dirt_elem)
#
# lightning_elem = air_elem + fire_elem
# print(lightning_elem)
#
# dust_elem = air_elem + earth_elem
# print(dust_elem)
#
# lava_elem = fire_elem + earth_elem
# print(lava_elem)




