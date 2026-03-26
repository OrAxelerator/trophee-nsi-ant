from cellule import get_cellule 
import random
from world import espace
from cellule import get_cellule
#from ..world import espace
from read_world import read_world

# ant_test = {
#       "pos" : [0,0],
#       "angle" : (0,1),
#       "have_food" : False

# }
# choix_fourmi = get_cellule(espace, ant_test, "filtered")

def dico_cases_getCel (choix, ant, espace) : 
    TousRead_world = {}
    # print("CHHHHHHHHHHHOIX", choix)

    for el in choix :

        # print("ELLLLLLLLLLL", el)
        case = read_world(ant, el, espace)
        if str(case) in TousRead_world.keys():
            TousRead_world[str(case)] += 1
        else:
            TousRead_world[str(case)] = 1

    return TousRead_world

def caclculTaux(choix:list, ant, espace, dico, mode) :
    
            
    # print("typr de dchoix 🍇", type(choix[0]))
    if len(choix) == 1 :
        # print("CHOIX VECTEUR", choix[0])
        return choix[0] ##################### A REVOIR OU ADAPTER LE CODE
    
    else :
        pheromone_rate = []
        choixXH = []
        for el in choix :
            # print("hmmmmmmmmmmmmmmmmm", el)
            if mode == "case" :
                if read_world(ant, el, espace) != "h" and read_world(ant, el, espace) != "X":
                    choixXH.append(el)
            if mode == "vector" :
                choixXH = choix
        # print("CHOIXXH", choixXH )
        
        for el in choixXH :
            weight = read_world(ant, el, espace)
            if mode == "case" :
                if weight == "f":
                    pheromone_rate.append(1/len(choixXH))
                else:
                    pheromone_rate.append(weight/len(choixXH))
            
            if mode == "vector":

                # print(weight)
                if weight == "f" or weight == "h" or weight == "X":
                    pheromone_rate.append(1/len(choixXH))
                else:
                    pheromone_rate.append(weight/len(choixXH))

        # print("choixXH", choixXH)
        # print("pheromone_rate", pheromone_rate)
        best_cellule = random.choices(  
            population = choixXH,
            weights = pheromone_rate ,
            k=1
        )
        # print('tpye de best cell 🗿🗿🗿🗿', type(best_cellule[0]))

        if type(choix[0]) == tuple:
            return best_cellule[0]
        else :
            return list(best_cellule[0])
            

def think(choix: list, ant: dict, espace:list, coef) -> tuple: 
    """
    renvoi le chemin le 'plus optimisé' selon les phéromones
    si la fourmi n'as pas accés a de la nourriture.
    Sinon renvoi le chemin direct a la nourriture si il y en a
    """
    food_path = []
    #choixXF = []
    #TtChoix =[]
    #print("choix : " , choix)
    #print("choaaaaaaaa : " , choix)
    #print("ANGLE", ant["angle"])
    choixXH = []
    for el in choix :
        if read_world(ant, el, espace) != "h" :
            choixXH.append(el)

    TousRead_world = dico_cases_getCel(choix, ant, espace)
    
    if ant["have_food"] == False and "f" in TousRead_world: # si elle a pas deja de la nourriture 
        for el in choixXH :
            #print("read_world",read_world(ant, el))
            if read_world(ant,el, espace) == "f":
                food_path.append(el) # récupere les emplacements de f
        #ant["angle"] = (-(ant["angle"][0]), -(ant["angle"][1])) #si sur food, prend direction inverse
        #print("Food Food Food")
        ant["have_food"] = True # dis qu'elle a à present de la nourriture
        #print("f/false")
        return random.choice(food_path) # choisi random un f autour de la fourmi si il y en a plusieurs

    else: 
        return caclculTaux(choix, ant, espace, TousRead_world, "case")
            
        
        
# print("think :",think(choix_fourmi, ant_test, espace))