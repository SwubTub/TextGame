import items

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
        return """
        You awake in a dark, square room, with a dark opening on each wall. The room is faintly lit by torches so you can barely make out your surroundings.
        """
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
        super().__init__(x, y)
    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))
class EmptyCavePath(Maptile):
    def intro_text(self):
        return """
        Another empty, bland part of the cave...
        """
    def modify_player(self, player):
        #Room has no action on player#
        pass
class LeaveCaveRoom(Maptile):
    def intro_text(self):
        return """
        You feel a breeze and start to see light. As you get closer you realize it's sunlight. You escaped!

        Well done
        """
    def modify_player(self, player):
        player.victory = True
class GoblinRoom(EnemyRoom):
    def __init__(self, x, y, enemy):
        super().__init__(x, y, enemies.Goblin())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A goblin jumps out from the shadows right in front of you!
            """
        else:
            return """
            A rotting goblin corpse is laying in front of you.
            """
class SkeletonRoom(EnemyRoom):
    def __init__(self, x, y, enemy):
        super().__init__(x, y, enemies.Skeleton())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A skeleton jumps you and is ready to kill you!
            """
        else:
            return """
            A pile of bones and a sword are sitting in the corner of the room.
            """
class OrcRoom(EnemyRoom):
    def __init__(self, x, y, enemy):
        super().__init__(x, y, enemies.Orc())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A large Orc is swinging his club, hungry for dinner!
            """
        else:
            return """
            A club is leaning against the wall, looks like the Orc is roaming.
            """
class FindMopRoom(LootRoom):
    def __init__(self, x, y, item):
        super().__init__(x, y, items.Mop())

    def intro_text(self):
        return """
        You catch a faint whiff of cleaning supplies. In the corner is a clean, shiny mop! You pick it up and add it to your inventory.
        """
class FindStickRoom(LootRoom):
    def __init__(self, x, y, item):
        super().__init__(x, y, items.Stick())

    def intro_text(self):
        return """
        A STICK! YAY! You proudly pick it up and carry along on your jolly travels.
        """
class FindSwordRoom(LootRoom):
    def __init__(self, x, y, item):
        super().__init__(x, y, items.Sword())

    def intro_text(self):
        return """
        A shiny sword is lying in the middle of the room, you pick it up and add it to your inventory.
        """
class FindGoldRoom(LootRoom):
    def __init__(self, x, y, item):
        super().__init__(x, y, items.Gold())

    def intro_text(self):
        return """
        You spot a gold coin on the ground, you add it to your inventory.
        """