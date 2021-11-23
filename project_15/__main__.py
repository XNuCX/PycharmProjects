from project_15.animals.birds import Owl, Hen
from project_15.animals.mammals import Mouse
from project_15.food import Meat, Vegetable, Fruit

owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)
hen = Hen("Harry", 10, 10)

veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)
mouse = Mouse("Pip", 10, "west")
print(mouse.make_sound())
print(mouse.feed(fruit))

