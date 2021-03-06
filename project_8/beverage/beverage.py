from project_8.product import Product


class Beverage(Product):
    def __init__(self, name, price, milliliters:float):
        super(Beverage, self).__init__(name, price)
        self.__milliliters = milliliters

    @property
    def milliliters(self):
        return self.__milliliters
    @milliliters.setter
    def milliliters(self, value):
        self.__milliliters = value