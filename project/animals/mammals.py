from project.animals.animal import Mammal
from project.food import Vegetable


class Mouse(Mammal):
    def __init__(self, *args, **kwargs):
        super(Mouse, self).__init__(*args, **kwargs)
    def make_sound(self):
        return f"Squeak"

    def feed(self, food):
        if type(food).__name__ != "Vegetable" and type(food).__name__ != "Fruit":
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        else:
            self.weight += 0.1
            self.times(food)


class Dog(Mammal):
    def __init__(self, *args, **kwargs):
        super(Dog, self).__init__(*args, **kwargs)
    def make_sound(self):
        return f"Woof!"
    def feed(self, food):
        if type(food).__name__ != "Meat":
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        else:
            self.weight += 0.4
            self.times(food)
class Cat(Mammal):
    def __init__(self, *args, **kwargs):
        super(Cat, self).__init__(*args, **kwargs)
    def make_sound(self):
        return f"Meow"
    def feed(self, food):
        if type(food).__name__ != "Vegetable" and type(food).__name__ != "Meat":
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        else:
            self.weight += 0.3
            self.times(food)
class Tiger(Mammal):
    def __init__(self, *args, **kwargs):
        super(Tiger, self).__init__(*args, *kwargs)

    def make_sound(self):
        return f"ROAR!!!"
    def feed(self, food):
        if type(food).__name__ != "Meat":
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        else:
            self.weight += 1.00
            self.times(food)