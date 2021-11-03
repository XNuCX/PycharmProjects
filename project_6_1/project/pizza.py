from .dough import Dough
from .topping import Topping


class Pizza:
    def __init__(self, name:str, dough:Dough, toppings_capacity:int):
        self._name = name
        self._dough = dough
        self._toppings_capacity = toppings_capacity
        self.toppings = {}
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("The name cannot be an empty string")
        else:
            self._name = value

    @property
    def dough(self):
        return self._dough

    @dough.setter
    def dough(self, value):

        if value is None :
            raise ValueError("You should add dough to the pizza")
        else:
            self._dough = value

    @property
    def toppings_capacity(self):
        return self._toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):

        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        else:
            self._toppings_capacity = value


    def add_topping(self, topping:Topping):
        if not len(self.toppings) == self.toppings_capacity:
            if topping.topping_type in self.toppings:
                self.toppings[topping.topping_type] += topping.weight
            else:

                self.toppings[topping.topping_type] = topping.weight

        else:
            raise ValueError("Not enough space for another topping")


    def calculate_total_weight(self):
        weight = 0
        for value in self.toppings.values():
            weight += value
        weight += self.dough.weight
        return weight

# tomato_topping = Topping("Tomato", 60)
# print(tomato_topping.topping_type)
# print(tomato_topping.weight)
#
# mushrooms_topping = Topping("Mushroom", 75)
# print(mushrooms_topping.topping_type)
# print(mushrooms_topping.weight)
#
# mozzarella_topping = Topping("Mozzarella", 80)
# print(mozzarella_topping.topping_type)
# print(mozzarella_topping.weight)
#
# cheddar_topping = Topping("Cheddar", 150)
#
# pepperoni_topping = Topping("Pepperoni", 120)
#
# white_flour_dough = Dough("White Flour", "Mixing", 200)
# print(white_flour_dough.flour_type)
# print(white_flour_dough.weight)
# print(white_flour_dough.baking_technique)
#
# whole_wheat_dough = Dough("Whole Wheat Flour", "Mixing", 200)
# print(whole_wheat_dough.weight)
# print(whole_wheat_dough.flour_type)
# print(whole_wheat_dough.baking_technique)
#
# p = Pizza("Margherita", whole_wheat_dough, 2)
#
# p.add_topping(tomato_topping)
# print(p.calculate_total_weight())
#
# p.add_topping(mozzarella_topping)
# print(p.calculate_total_weight())
#
# p.add_topping(mozzarella_topping)

