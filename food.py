from cellule import get_cellule
from world import espace
from read_world import read_world


ant1 = (0,0) # y, x
ant2 = (4,11)
ant3 = (11,11)

possi = get_cellule(espace, ant1)

print(possi)
def food(possibility, ant):
    for choix in possibility :   
        if read_world(ant, choix) == "f":
            print("Food Food Food")
            return True 


food(possi, ant1)