from world import espace

def read_world(ant:dict, direction:tuple | dict):
    """
    calcule la position de ant + direction
    in : tuple or array
    out : the actual value of espace[y][x]
    """
    y = ant["pos"][0] + direction[0] 
    x = ant["pos"][1] + direction[1]
    return espace[y][x]