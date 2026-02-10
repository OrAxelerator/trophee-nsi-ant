import random
from cellule import get_cellule
from world import espace, LARGEUR, HAUTEUR
from draw import draw
import read_world as read_world
from chose2_0 import think
from unlock import unblock

from parametre import ant_array
from chose_cellule import choose
from food import food
ant1 = {
    "pos" : [0,0],
    "angle" : (0,1),
    "have_food": False
}
#ant_array = [ant1]#TEST
print(ant_array)


def move(choix:tuple, ant:dict):
    print("choix de move() : ", choix)
    #print("ant[pos] : ", ant["pos"])
    pheromones(espace, ant)
    #espace[ant["pos"][0]][ant1[1]] = 0
    #espace[ant1["pos"][0]][ant1["pos"][1]] += 1
    ant["pos"][0] += choix[0] 
    ant["pos"][1] += choix[1]
    print("angle : ", ant["angle"])

def pheromones(espace, ant:dict):
    """pose phéromones a la position de la fourmi avant son déplacement
    seulement si elle a de la nourriture"""
    if ant["have_food"]:
        print("pos :", espace[ant["pos"][0]][ant["pos"][1]])
        if espace[ant["pos"][0]][ant["pos"][1]] != "f" :
            espace[ant["pos"][0]][ant["pos"][1]] += 1 

print("LANCEMENT =========================================================================== ")
while True:
    input()
    for ant in ant_array:
        print("--------------------------------------------------------------------")
        choix = get_cellule(espace,ant) # choix "légal"
        if choix == [] :
            ant["angle"] = unblock(espace, ant)
            choix = get_cellule(espace,ant)

        print("tout les choix", choix)
        brain_fourmi = think(choix, ant)
        print("brain : ", brain_fourmi)#devrait sortir que 1 ELEMENT
        move(brain_fourmi, ant)
        #
        #if food(choix, ant) != False and ant["have_food"] == False:
        #    print("ant have food")
        #    move(food(choix, ant), ant)#allez a nour
        #else:
        #    print("ant pas de food")
        #    dir = choose(choix, ant)
        #    print(dir)
        #    move(dir, ant)
    draw(espace, ant_array)
    print("----------------")
        #move(choix, ant)
        #espace[ant["pos"][0]][ant["pos"][1]] = "F"
        #draw(espace)
        #print("============")
        #input("...")

print(ant_array)