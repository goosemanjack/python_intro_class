
class Hero:
    name = "My Guy"
    level = 0

    def __init__(self, name):
        self.weapons = []

    def add_weapon(self, weapon):
        self.weapons.append(weapon)



h = Hero("Bob")
h.add_weapon("Spear")
