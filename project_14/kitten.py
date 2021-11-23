from project_14.cat import Cat


class Kitten(Cat):
    def __init__(self, *args, **kwargs):
        super(Kitten, self).__init__(*args, **kwargs)
        self.gender = "Female"
    def make_sound(self):
        return f"Meow"

