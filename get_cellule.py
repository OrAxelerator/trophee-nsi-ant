from main import espace
ant1 = (0,0)
ant2 = (4,11)
ant3 = (11,11)


def get_cellule(world, tuple):
    choices = {
        "right" : (0,1),
        "down" :(-1,0),
        "left" :(0,-1),
        "up": (1,0)
        }
    
    interdiction=[]
    if tuple[0] == 0:
        interdiction.append(choices["up"])
    if tuple[0] == len(world[0]) - 1 :
        interdiction.append(choices[ "down"])
    if tuple[1] == 0 :
        interdiction.append(choices["left"])
    if tuple[1] == len(world[0]) - 1:
        interdiction.append(choices["right"])

    possibility = []
    for el in choices:
        if choices[el] != "X" and choices[el] not in interdiction:
            possibility.append(choices[el])
    return possibility

get_cellule(espace,ant1 )
get_cellule(espace,ant2 )
get_cellule(espace,ant3 )
