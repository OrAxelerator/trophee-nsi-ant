from world import espace

def read_world(ant, direction):
    """
    calcule la position de ant + direction
    in : tuple or array
    out : the actual value of espace[y][x]
    """
    y = ant[0] + direction[0] 
    x = ant[1] + direction[1]
    return espace[y][x]