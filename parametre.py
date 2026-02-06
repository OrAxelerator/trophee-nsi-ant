import random
from cellule import get_cellule

nb_ant = 1  #int(input("nb de fourmi : "))
#world_selection = input("selection monde \n1 - monde aléatoire\n2 - monde prédéfini")


ant = { # exemple
    "pos" : (3, 3),
    "angle" : (0,1),
    "have_food" : False
}


def init_ant():
    """creer un array de n fourmis"""
    forumi_array = []
    for i in range(nb_ant):
        forumi_array.append({
        "pos" : [0,0], # mettre x, y fourmilière
        "angle" : (random.choice((-1, 0, 1)), random.choice((-1, 0, 1))),  # Si fourmilere dans coins ou proche d'obstace : prob, use get_cellule
    
        "have_food" : False
        })
        # Pour empecher fourmi d'avoir angle nul et de pouvoir se déplacer librement
        if forumi_array[i]["angle"] == (0,0):
            # choisi une valeur au hasard de angle pour y rajouter 1 ou -1
            forumi_array[i]["angle"][random.choice((0,1))] += random.choice((-1, 1))

    return forumi_array
    
ant_array = init_ant()


#print(init_ant())