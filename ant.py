import random

def init_ant(hill, nb_fourmi):
    """creer un array de n fourmis"""
    angle_possi = [(-1, 0), (0, 1), (1,0), (0, -1)]
    fourmi_array = []
    for i in range(nb_fourmi):
        fourmi_array.append({
        "pos" : [hill[0], hill[1]], # mettre x, y fourmilière
        "angle" : random.choice(angle_possi),  # Si fourmilere dans coins ou proche d'obstace : prob, use get_cellule
        "have_food" : False
        })
        # Pour empecher fourmi d'avoir angle nul et de pouvoir se déplacer librement

    return fourmi_array