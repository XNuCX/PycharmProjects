import abc

class Person(abc.ABC):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return Person(self.name,other.surname)

    def __repr__(self):
        return f"{self.name} {self.surname}"

class Group:
    def __init__(self, name:str, people):
        self.name = name
        self.people = people
    def __len__(self):
        return len(self.people)


    def __add__(self,other):

        name = f"{self.name} {other.name}"
        people = self.people + other.people
        return Group(name, people)

    def __repr__(self):
        people = [p.__repr__() for p in self.people]
        return f"Group {self.name} with members {', '.join(people)}"

    def __getitem__(self, item):
        people = []

        for i, p in enumerate(self.people):
            repr_1 = f"Person {i}: {p.__repr__()}"
            people.append(repr_1)
        return people[item]


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group)
print(third_group[0])

for person in third_group:
    print(person)

