from tiles import Maptile

_world = {}
starting_position = (0, 0)
 
def load_tiles():
    """Parses a file that describes the world space into the _world object"""
    with open('game/resources/map.txt', 'r') as f:
        rows = f.readlines()
    x_max = len(rows[0].split('\t'))
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            Maptile = cols[x].replace('\n', '')
            if Maptile == 'StartingRoom':
                global starting_position
                starting_position = (x, y)
            _world[(x, y)] = None if Maptile == '' else getattr(__import__('tiles'), Maptile)(x, y)

def tile_exists(x, y):
    return _world.get((x, y))