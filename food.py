from cellule import get_cellule
from world import espace
from read_world import read_world


ant1 = { # exemple
    "pos" : (0, 0),
    "angle" : (0,1),
    "have_food" : False
}
possi = get_cellule(espace, ant1)

#print(possi) #test
def food(possibility, ant) -> tuple | bool:
    """
    Si aucune nouttiure n'est présente, renvoi False
    Sinon renvoi la position de la nourriture en tupple
    """
    for choix in possibility :
        #print(read_world(ant, choix))
        if read_world(ant, choix) == "f":
            ant["angle"] = (-(ant["angle"][0]), -(ant["angle"][1])) #si sur food, prend direction inverse
            print("Food Food Food")
            ant["have_food"] = True
            
            return choix
        else:
            return False



#print(food(possi, ant1)) #test$
#food(possi, ant1)
#print(ant1["angle"])