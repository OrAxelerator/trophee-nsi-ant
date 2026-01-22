from world import espace
from read_world import read_world

# to delete
ant1 = (0,0)
ant2 = (4,11)
ant3 = (11,11)


def get_cellule(world, ant):
    choices = {
        "up": (-1,0),
        "down" :(1,0),
        "left" :(0,-1),
        "right" : (0,1)
    }
    
    interdiction=[]
    if ant[0] == 0:
        interdiction.append(choices["up"])
    if ant[0] == len(world[0]) - 1 :
        interdiction.append(choices["down"])
    if ant[1] == 0 :
        interdiction.append(choices["left"])
    if ant[1] == len(world[0]) - 1:
        interdiction.append(choices["right"])

    possibility = []
    for el in choices:
        if choices[el] not in interdiction:

            if read_world(ant, choices[el]) != "X" :
                possibility.append(choices[el])

    return possibility


#print(get_cellule(espace, ant1)) #test