class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, milliliters):
        if self.quantity + milliliters <= self.size:
            self.quantity += milliliters
        return
    def status(self):
        free_space = self.size - self.quantity
        return free_space
