from project_8.beverage.beverage import Beverage


class ColdBeverage(Beverage):
    def __init__(self, name, price, milliliters):
        super(ColdBeverage, self).__init__(name, price, milliliters)
