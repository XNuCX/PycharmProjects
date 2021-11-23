from project_14.animal import Animal


class Cat(Animal):
    def __init__(self, *args, **kwargs):
        super(Cat, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {type(self).__name__}"
    def make_sound(self):
        return f"Meow meow!"