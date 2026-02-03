import random
from cellule import get_cellule
from world import espace, LARGEUR, HAUTEUR
from draw import draw
import read_world

from parametre import ant_array
print(ant_array )
from chose_cellule import choose
from food import food



def move(choix:tuple, ant:dict):
    print("choix : ", choix)
    print(ant)
    print("ant[pos] : ", ant["pos"])
    pheromones(espace, ant)
    #espace[ant["pos"][0]][ant1[1]] = 0
    #espace[ant1["pos"][0]][ant1["pos"][1]] += 1
    ant["pos"][0] += choix[0]
    ant["pos"][1] += choix[1]


def pheromones(espace, ant:dict):
    """pose phéromones a la position de la fourmi avant son déplacement
    seulement si elle a de la nourriture"""
    if ant["have_food"]:
        espace[ant["pos"][0]][ant["pos"][1]] += 1 


print("LANCEMENT =========================================================================== ")
while True:
    input()
    for ant in ant_array:
        print("--------------------------------------------------------------------")
        choix = get_cellule(espace,ant) # choix "légal"
        if food(choix, ant) != False and ant["have_food"] == False:
            print("ant have food")
            move(food(choix, ant), ant)#allez a nour
        else:
            print("ant pas de food")
            dir = choose(choix, ant)
            print(dir)
            move(dir, ant)
    print("----------------")
    draw(espace)
        #move(choix, ant)
        #espace[ant["pos"][0]][ant["pos"][1]] = "F"
        #draw(espace)
        #print("============")
        #input("...")

print(ant_array)