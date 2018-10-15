import items, enemies

class Maptile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def intro_text(self):
    raise NotImplementedError()

def modify_player(self, player):
        raise NotImplementedError()
class StartingRoom(Maptile):
    def intro_text(self):
        return '''
        You awake in a dark, square room, with a dark opening on each wall. The room is faintly lit by torches so you can barely make out your surroundings.'''
    def modify_player(self, player):
        #Room has no action on player#
        pass
class LootRoom(Maptile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)
class EnemyRoom(Maptile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super()__init__(x, y)
    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))
        
