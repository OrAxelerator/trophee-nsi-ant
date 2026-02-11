from world import espace
from read_world import read_world


ant = { # exemple
    "pos" : (3, 2),
    "angle" : (0,-1),
    "have_food" : True
}

def get_cellule(world, ant: dict) -> list:
    """renvoi la liste des positions possibles autour de la fourmi"""
    choices = {
        "up": (-1,0),
        "up-right": (-1,1),
        "up-left": (-1,-1),
        "down" :(1,0),
        "down-right" :(1,1),
        "down-left" :(1,-1),
        "left" :(0,-1),
        "right" : (0,1),
    }

    interdiction=[]
    if ant["pos"][0] == 0:
        interdiction.append(choices["up"])
        interdiction.append(choices["up-right"])
        interdiction.append(choices["up-left"])
    if ant["pos"][0] == len(world[0]) - 1 :
        interdiction.append(choices["down"])
        interdiction.append(choices["down-left"])
        interdiction.append(choices["down-right"])
    if ant["pos"][1] == 0 :
        interdiction.append(choices["left"])
        interdiction.append(choices["down-left"])
        interdiction.append(choices["up-left"])
    if ant["pos"][1] == len(world[0]) - 1:
        interdiction.append(choices["right"])
        interdiction.append(choices["up-right"])
        interdiction.append(choices["down-right"])


    possibility = []
    Read_world = []
    choix = []

    for el in choices :
        if choices[el] not in interdiction:
            if read_world(ant, choices[el], world) != "X" :
                Read_world.append(read_world(ant, choices[el], world))
                possibility.append(choices[el])
        
    print("read read", Read_world)
    print("possibility",possibility)

    
    if "f" not in Read_world or ant["have_food"] == True:

        coef = 0 # indiceou se situe le 1 ou -1 dans angle
        if ant["angle"][0] == -1 or ant["angle"][0] == 1:
            coef = 0
        elif ant["angle"][1] == -1 or ant["angle"][1] == 1:
            coef = 1

        for el in possibility :
                print("el",el)
                if (el[coef] == ant["angle"][coef]):
                        choix.append(el)

        return choix #return par rapport à l'angle
    
    if "f" in Read_world and ant["have_food"] == False:
            return possibility # return toutes les possibilités autour de la fourmi


#print(detectF(espace, ant))
print(get_cellule(espace, ant)) #test