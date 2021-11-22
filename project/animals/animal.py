import abc

class Animal(abc.ABC):
    def __init__(self, name:str, weight:float, food_eaten=0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten
    @abc.abstractmethod
    def make_sound(self):
        pass
    @abc.abstractmethod
    def feed(self, food):

        pass
    def times(self, food):
        self.food_eaten += food.quantity
class Bird(Animal):
    def __init__(self, name, weight, wing_size:float):
        super(Bird, self).__init__(name, weight, food_eaten=0)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"
class Mammal(Animal):
    def __init__(self, name, weight, living_region:str):
        super(Mammal, self).__init__(name, weight, food_eaten=0)
        self.living_region = living_region
    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
