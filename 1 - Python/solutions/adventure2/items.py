


from entities import Entity


class Item(Entity):
    def __init__(self, name, symbol, loc_i, loc_j, attack, defense):
        super().__init__(name, symbol, loc_i, loc_j)
        self.attack = attack
        self.defense = defense


class Sword(Item):
    def __init__(self, loc_i, loc_j, attack_modifier):
        super().__init__('sword', '☨', loc_i, loc_j, attack_modifier, 0)


class Shield(Item):
    def __init__(self, loc_i, loc_j, defense_modifier):
        super().__init__('sword', '☨', loc_i, loc_j, 0, defense_modifier)



