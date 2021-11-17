from project_8.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.5
    def __init__(self,name,caffeine:float):
        super(Coffee, self).__init__(name, price=self.PRICE, milliliters=self.MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine
    @caffeine.setter
    def caffeine(self, value):
        self.__caffeine = value

