import random

def init_ant(nb_fourmi:int ,hill:list):
    """creer un array de n fourmis"""
    angle_possi = [(-1, 0), (0, 1), (1,0), (0, -1)]
    fourmi_array = []
    for _ in range(nb_fourmi):
        fourmi_array.append({
        "pos" : [hill[0], hill[1]], # mettre x, y fourmilière
        "angle" : random.choice(angle_possi),  # Si fourmilere dans coins ou proche d'obstace : prob, use get_cellule
        "have_food" : False,
        "demi_tour": False,
        "mode" : "home",
        "side" : 0
        })
        # Pour empecher fourmi d'avoir angle nul et de pouvoir se déplacer librement

    return fourmi_array