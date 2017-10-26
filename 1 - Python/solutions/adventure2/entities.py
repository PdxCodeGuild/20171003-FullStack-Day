

class Entity:
    def __init__(self, name, symbol, loc_i, loc_j):
        self.name = name
        self.symbol = symbol
        self.loc_i = loc_i
        self.loc_j = loc_j


class LivingEntity(Entity):
    def __init__(self, name, symbol, loc_i, loc_j, health, attack, defense):
        super().__init__(name, symbol, loc_i, loc_j)
        self.health = health
        self.attack = attack
        self.defense = defense
        self.inventory = []

    def calculate_attack(self):
        attack = self.attack
        for item in self.inventory:
            attack += item.attack
        return attack

    def calculate_defense(self):
        defense = self.defense
        for item in self.inventory:
            defense += item.defense
        return defense


class Player(LivingEntity):
    def __init__(self, loc_i, loc_j):
        super().__init__('Player', '☻', loc_i, loc_j, health=10, attack=1, defense=1)


class Skeleton(LivingEntity):
    def __init__(self, loc_i, loc_j):
        super().__init__('Skeleton', '☠', loc_i, loc_j, health=3, attack=1, defense=1)




