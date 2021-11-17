from project_8.beverage.beverage import Beverage


class HotBeverage(Beverage):
    def __init__(self, name, price, milliliters):
        super(HotBeverage, self).__init__(name, price, milliliters)
