"""
Задача 1. Налоги
Реализуйте иерархию классов, описывающих имущество налогоплательщиков.
Она должна состоять из базового класса Property
и производных от него классов Apartment, Car и CountryHouse.
Базовый класс должен иметь атрибут worth (стоимость), который передаётся в конструктор,
и метод расчёта налога,
переопределённый в каждом из производных классов.
Налог на квартиру вычисляется как 1/1000 её стоимости, на машину — 1/200, на дачу — 1/500.
Каждый дочерний класс должен иметь конструктор с одним параметром,
передающий свой параметр конструктору базового класса.

Разработайте интерфейс программы.
Пусть она запрашивает у пользователя количество его денег и стоимость имущества,
а затем выдаёт налог на соответствующее имущество и показывает,
сколько денег ему не хватает (если это так).
"""


class Property:
    """
    class Property contains property worth

    Args:
        worth (float): worth of property
        Attributes:
            tax_rate (float): tax rate

    """

    tax_rate: float
    _worth: float

    def __init__(self, worth: float):
        self._worth = worth

    @property
    def tax(self):
        """Get tax"""
        return round(self._worth * self.tax_rate, 2)

    def __str__(self):
        return f'Worth of property: {self._worth}'


class Apartment(Property):
    """tax_rate: = 0.001"""

    tax_rate = 0.001

    def __init__(self, worth: float):
        super().__init__(worth)


class Car(Property):
    """tax_rate = 0.005"""

    tax_rate = 0.005

    def __init__(self, worth: float):
        super().__init__(worth)


class CountryHouse(Property):
    """tax_rate = 0.002"""

    tax_rate = 0.002

    def __init__(self, worth: float):
        super().__init__(worth)


person_money = float(input('Amount of your money: '))
apartment = Apartment(float(input('Worth of your apartment: ')))
car = Car(float(input('Worth of your car: ')))
country_house = CountryHouse(float(input('Worth of your country house: ')))

person_properties = {prop: prop.tax for prop in [apartment, car, country_house]}
total_taxes = sum(person_properties.values())
print(f'Car tax: {person_properties[car]}\n'
      f'Apartment tax: {person_properties[apartment]}\n'
      f'Country house tax: {person_properties[country_house]}\n'
      f'Total taxes: {total_taxes}')

if person_money < total_taxes:
    print(f'You don\'have enough money to pay taxes\n'
          f'You are in need of addition {total_taxes - person_money} euros')
else:
    print('You can pay off all of your taxes completely')



