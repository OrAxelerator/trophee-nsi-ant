

def read_world(ant:dict, direction:tuple, espace:list | dict):
    """
    calcule la position de ant + direction
    in : tuple or array
    out : the actual value of espace[y][x]
    """
    y = ant["pos"][0] + direction[0] 
    x = ant["pos"][1] + direction[1]
    if 0 <= x <= len(espace[0])-1 and 0 <= y <= len(espace)-1 :
        return espace[y][x]
    else :
        return "out"


# print(read_world(ant1, (-1, 0), espace))