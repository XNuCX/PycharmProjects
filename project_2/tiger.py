from .animal import Animal
class Tiger(Animal):
    def __init__(self, name:str, gender:str, age:int):
        super(Tiger, self).__init__(name, gender, age, money_for_care=45)