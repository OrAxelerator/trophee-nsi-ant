import random
from cellule import get_cellule
from world import espace, LARGEUR, HAUTEUR
from draw import draw
from read_world import read_world
from chose2_0 import think
from unlock import unblock
from chose_cellule import choose
from backToHome2_0 import back_home
ant1 = {
    "pos" : [0,0],
    "angle" : [0,1],
    "have_food": False
}
#ant_array = [ant1]#TEST
hill = {
    "pos" : [0,0]
}

def move(choix:tuple, ant:dict):
    print("choix de move() : ", choix)
    ant["pos"][0] += choix[0] 
    ant["pos"][1] += choix[1]

def pheromones(espace, ant:dict):
    """pose phéromones a la position de la fourmi avant son déplacement
    seulement si elle a de la nourriture"""
    if ant["have_food"]:
        print("pos :", espace[ant["pos"][0]][ant["pos"][1]])
        if espace[ant["pos"][0]][ant["pos"][1]] not in ("f","h") :
            espace[ant["pos"][0]][ant["pos"][1]] += 1 

print("LANCEMENT =========================================================================== ")
FOOD = 0
nbangleOpposed = 0
while True:
    for ant in ant_array:
        if ant["have_food"]:
            if ant["pos"] != hill:
                nb_tour = 0 if read_world(ant, (0,0), espace) == "f" else 1 
                back_Home = back_home(ant, hill, espace, nb_tour) 
                case = back_Home
                move(case, ant) 
                if ant["pos"] == hill["pos"]:
                    FOOD +=1
                    ant["have_food"] = False
                    ant["angle"] = (-(ant["angle"][0]), -(ant["angle"][1]))
        else: 
            print("--------------------------------------------------------------------")
            choix = get_cellule(espace,ant, "filtered") # choix "légal"
            if choix == [] :
                ant["angle"] = unblock(espace, ant)
                choix = get_cellule(espace, ant, "filtered")
            brain_fourmi = think(choix, ant, espace)
            print("brain : ", brain_fourmi)#devrait sortir que 1 ELEMENT
            move(brain_fourmi, ant)
    draw(espace, ant_array)
    print("----------------")