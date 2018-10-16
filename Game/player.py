import items, tiles, actions, world

class Player():
    def __init__(self):
        self.inventory = [items.gold(5), items.stick(1)]
        self.hp = 100
        self.location_x, self.location_y, = world.starting_position
        self.victory = False

    def is_alive(self):
        return self.hp > 0
    
    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y) .intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)
    
    def move_east(self):
        self.move(dx=1, dy=0)
    
    def move_west(self):
        self.move(dx=-1, dy=0)
    
    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max.dmg:
                    max.dmg = i.damage
                    best_weapon = i

        print('You use {} against {}!'.format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print('You killed {}!'.format(enemy.name))
        else:
            print('{} HP is []!'.format(enemy.name, enemy.hp))

def adjacent_moves(self):
    """Returns all moves for adjacent tiles."""
    moves = []
    if world.tile_exists(self.x + 1, self.y):
        moves.append(actions.MoveEast())
    if world.tile_exists(self.x - 1, self.y):
        moves.append(actions.MoveWest())
    if world.tile_exists(self.x, self.y - 1):
        moves.append(actions.MoveNorth())
    if world.tile_exists(self.x, self.y + 1):
        moves.append(actions.MoveSouth())
    return moves

def available_actions(self):
    """Returns all available actions in this room."""
    moves = self.adjacent_moves()
    moves.append(actions.ViewInventory())

    return moves

def do_action(self, action, **kwargs):
    action_method = getattr(self, action.method.__name__)
    if action_method:
        action_method(**kwargs)

import random #Note the new import!
import items, world
 
class Player:
 
    def flee(self, tile):
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

class Flee(Action):
    def __init__(self, tile):
        super().__init__(method=Player.flee, name="Flee", hotkey='f', tile=tile)

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
 
    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))
 
    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()