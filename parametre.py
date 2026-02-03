import random
from cellule import get_cellule

nb_ant = 2  #int(input("nb de fourmi : "))
#world_selection = input("selection monde \n1 - monde aléatoire\n2 - monde prédéfini")


ant = { # exemple
    "pos" : (3, 3),
    "angle" : (0,1),
    "have_food" : False
}


def init_ant():
    forumi_array = []
    for i in range(nb_ant):
        forumi_array.append({
        "pos" : (0,0), # mettre x, y fourmilière
        "angle" : (random.randint(-1, 1), random.randint(-1, 1)),  # Si fourmilere dans coins ou proche d'obstace : prob, use get_cellule
        "have_food" : False
        })
    return forumi_array
    
ant_array = init_ant()


#print(init_ant())




