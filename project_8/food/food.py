from project_8.product import Product


class Food(Product):
    def __init__(self, name, price, grams: float):
        super(Food, self).__init__(name, price)
        self.__grams = grams

    @property
    def grams(self):
        return self.__grams

    @grams.setter
    def grams(self, value):
        self.__grams = value
