from .caretaker import Caretaker
from .cheetah import Cheetah
from .keeper import Keeper
from .lion import Lion
from .tiger import Tiger
from .vet import Vet


class Zoo:
    _workers = ["Keeper", "Caretaker", "Vet"]
    _animals = ["Lion", "Tiger", "Cheetah"]
    _group_workers = ["Keepers", "Caretakers", "Vets"]
    _group_animals = ["Lions", "Tigers", "Cheetahs"]
    def __init__(self, name:str, budget:int, animal_capacity:int, workers_capacity:int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity == 0:
            return "Not enough space for animal"
        elif self.__budget >= price:
            self.animals.append(animal)
            self.__budget -= price
            self.__animal_capacity -= 1
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        else:
            return "Not enough budget"
    def hire_worker(self, worker):
        if self.__workers_capacity == 0:
            return "Not enough space for worker"
        else:
           self.workers.append(worker)
           # self.__workers_capacity -= 1
           return f"{worker.name} the {type(worker).__name__} hired successfully"

    def fire_worker(self, worker_name):
        worker = [i for i, n in enumerate(self.workers) if n.name == worker_name]
        try:
            del self.workers[worker[0]]


        except IndexError:
            return f"There is no {worker_name} in the zoo"
        else:
            self.__workers_capacity += 1
            return f"{worker_name} fired successfully"
    def pay_workers(self):
        sum_salaries = sum([sal.salary for sal in self.workers])
        if self.__budget >= sum_salaries:
            self.__budget -= sum_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"
    def tend_animals(self):
        sum_money_for_care = sum([mfc.money_for_care for mfc in self.animals])
        if self.__budget >= sum_money_for_care:
            self.__budget -= sum_money_for_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."
    # @property
    # def profit(self):
    #     return self.__budget
    # @profit.setter
    def profit(self, amount):
        print(self.__budget + amount)
        self.__budget += amount
    def animals_status(self):
        return self.printing("animals", self.animals, self._animals, self._group_animals)

    def workers_status(self):
        return self.printing("workers", self.workers, self._workers, self._group_workers)
    def printing(self, kind, lists, names, group):
        format_printing = ''
        for i, t in enumerate(names):
            format_printing += f"\n----- {len([n for n in lists if t == type(n).__name__])} {group[i]}:"
            for obj in [n for n in lists if t == type(n).__name__]:
                format_printing += f"\n{obj.__repr__()}"
            # format_printing += "\n…"

        return f"You have {len(lists)} {kind}{format_printing}"
