class Item():
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name = 'Gold',
                         description = 'A round coin with [] stamped on the front.'.format(str(self.amt)),value=self.amt)

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value,)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Stick(Weapon):
    def __init__(self):
        super().__init__(name = 'Stick',
                         description = 'A stick',
                         value = 0,
                         damage = 3)
class Sword(Weapon):
    def __init__(self):
        super().__init__(name = 'Sword',
                         description = 'A sword with a fine point tip, a little rust is starting to form near the hilt',
                         value = 5,
                         damage = 7)
class Mop(Weapon):
    def __init__(self):
        super().__init__(name = 'Mop',
                         description = 'A superior weapon used only by the most daring, brave warriors',
                         value = 10,
                         damage = 15)
class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

class Goblin(Enemy):
    def __init__(self):
        super().__init__(name = 'Goblin', hp = 10, damage = 3)

class Skeleton(Enemy):
    def __init__(self):
        super().__init__(name = 'Skeleton', hp = 15, damage = 5)

class Orc(Enemy):
    def __init__(self):
        super().__init__(name = 'Orc', hp = 20, damage = 7)
