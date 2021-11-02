from .worker import Worker

class Vet(Worker):
    def __init__(self, name, age, salary):
        super(Vet, self).__init__(name, age, salary)