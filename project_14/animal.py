import abc
class Animal(abc.ABC):
    def __init__(self, name, age, gender=None):
        self.name = name
        self.age = age
        self.gender = gender
    @abc.abstractmethod
    def make_sound(self):
        pass
    @abc.abstractmethod
    def __repr__(self):
        pass

