from project.animals.animal import Bird


class Owl(Bird):
    def __init__(self, *args, **kwargs):
        super(Owl, self).__init__(*args, **kwargs)
    def make_sound(self):
        return f"Hoot Hoot"
    def feed(self, food):
        if type(food).__name__ != "Meat":
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        else:
            self.weight += food.quantity * 0.25
            self.times(food)

class Hen(Bird):
    def __init__(self, *args, **kwargs):
        super(Hen, self).__init__(*args, **kwargs)
    def make_sound(self):
        return f"Cluck"
    def feed(self, food):
        self.weight += food.quantity * 0.35
        self.times(food)
