class Hero:
    def __init__(self, name:str, health:int):
        self.name = name
        self.health = health

    def defend(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            return f"{self.name} was defeated"
        else:
            return

    def heal(self, amount):
        self.health += amount
        return

hero = Hero(health=100, name="Peter")
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))
