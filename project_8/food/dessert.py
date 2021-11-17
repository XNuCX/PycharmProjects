from project_8.food.food import Food


class Dessert(Food):
    def __init__(self, name, price, grams, calories:float):
        super(Dessert, self).__init__(name, price, grams)
        self.__calories = calories

    @property
    def calories(self):
        return self.__calories

    @calories.setter
    def calories(self, value):
        self.__calories = value
