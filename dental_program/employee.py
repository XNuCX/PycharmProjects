from dental_program.person import Person


class Employee(Person):

    def __init__(self):
        super().__init__()

a = Employee()

a.age = "01/01/2023"
print(a.age)