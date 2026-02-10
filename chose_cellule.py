import random 
from cellule import get_cellule
from world import espace
from read_world import read_world
ant1 = { # exemple
    "pos" : (0, 0),
    "angle" : (0,1),
    "have_food" : False
}
choix = get_cellule(espace, ant1)

#print(read_world(ant1, (0,0)))
print("choix : ", choix)
#ant, choix


def choose( choix : list, ant: dict) -> tuple:
    """
    choix: [(0, 1) ...]
    ant : dict
    choisi quel case prendre en fonction des phéromones
    """
    res = []
    choixXF= []

    for el in choix : 
      if read_world(ant, el) != "f" :
        choixXF.append(el)

    for el in choixXF :
        #print(el, read_world(ant, el))
            res.append(read_world(ant, el) / len(choixXF))
        #print (res)

    #print("res:", res)
    el =  random.choices(
        population=choixXF,
        weights=res,
        k=1
    )
    return el[0] # tupple

#print(choose(choix, ant1))