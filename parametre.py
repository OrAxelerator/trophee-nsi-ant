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
    angle_possi = [(-1, 0), (0, 1), (1,0), (0, -1)]
    fourmi_array = []
    for i in range(nb_ant):
        fourmi_array.append({
        "pos" : [0,0], # mettre x, y fourmilière
        "angle" : random.choice(angle_possi),  # Si fourmilere dans coins ou proche d'obstace : prob, use get_cellule
        "have_food" : False
        })
        # Pour empecher fourmi d'avoir angle nul et de pouvoir se déplacer librement

    return fourmi_array
    
ant_array = init_ant()


#print(init_ant())