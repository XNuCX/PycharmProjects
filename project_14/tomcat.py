from project_14.cat import Cat


class Tomcat(Cat):
    def __init__(self, name, age, gender="Male"):
        super(Tomcat, self).__init__(name, age, gender)
        self.gender = "Male"
    def make_sound(self):
        return f"Hiss"
    # @property
    # def gender(self):
    #     return self.gender
    # @gender.setter
    # def gender(self, value="Male"):
    #     self.gender = value
