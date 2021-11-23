from project_14.animal import Animal


class Dog(Animal):
    def __init__(self, *args, **kwargs):
        super(Dog, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {type(self).__name__}"
    def make_sound(self):
        return f"Woof!"