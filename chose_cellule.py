import random 
from cellule import get_cellule
from world import espace
from read_world import read_world

def choose( choix : list, ant: dict, coef:int) -> tuple:
    """
    choix: [(0, 1) ...]
    ant : dict
    choisi quel case prendre en fonction des phéromones
    """
    res = []
    choixXF= []
    somme = 0
    for el in choix : 
      if read_world(ant, el) not in ("f", "h", "X"):
        choixXF.append(el)
        somme += el ** coef

    poids = [] 
    for c in choix:    
        poids.append( c ** coef / somme )
    
    # for el in choixXF :
    #         res.append(read_world(ant, el) / len(choixXF))

    #print("res:", res)
    el =  random.choices(
        population=choixXF,
        weights=poids,
        k=1
    )
    return el[0] # tupple
