import abc
class Vehicle(abc.ABC):
    @abc.abstractmethod
    def drive(self, *args, **kwargs):
        pass
    @abc.abstractmethod
    def refuel(self, *args, **kwargs):
        pass

class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption ):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        self.fuel_consumption = self.fuel_consumption + 0.9
        if distance * self.fuel_consumption <= self.fuel_quantity:
            self.fuel_quantity -= distance * self.fuel_consumption
        return

    def refuel(self, fuel):
        self.fuel_quantity += fuel
        return

class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption ):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        self.fuel_consumption = self.fuel_consumption + 1.6
        if distance * self.fuel_consumption <= self.fuel_quantity:
            self.fuel_quantity -= distance * self.fuel_consumption
        return


    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95
        return

car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
