from project_8.food.food import Food


class MainDish(Food):
    def __init__(self, name, price, grams):
        super(MainDish, self).__init__(name, price, grams)
