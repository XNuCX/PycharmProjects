from .worker import Worker

class Caretaker(Worker):
    def __init__(self, name, age, salary):
        super(Caretaker, self).__init__(name, age, salary)
