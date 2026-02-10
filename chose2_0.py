from cellule import get_cellule
from world import espace
from read_world import read_world
#from parametre import ant_array
import random

ant_test = {
      "pos" : (0,0),
      "angle" : (0,1),
      "have_food" : False
}

choix_fourmi = get_cellule(espace, ant_test)
def think(choix: list, ant: dict) -> tuple: 

    """
    renvoi le chemin le 'plus optimisé' selon les phéromones
    si la fourmi n'as pas accés a de la nourriture.
    Sinon renvoi le chemin direct a la nourriture si il y en a
    """
    food_path = []
    pheromone_rate = []
    choixXF = []
    #print("choix : " , choix)
    for el in choix : 
        if read_world(ant, el) == "f" : 
            if ant["have_food"] == False: 
                food_path.append(el) 
                ant["angle"] = (-(ant["angle"][0]), -(ant["angle"][1])) #si sur food, prend direction inverse
                #print("Food Food Food")
                ant["have_food"] = True 

            return random.choice(food_path) # tupple
        
        elif read_world(ant, el) != "f" : 
            choixXF.append(el)
            #print("el-ajouté")
            pheromone_rate.append(read_world(ant, el) / len(choixXF))
            #print("-----")
            #print(f'choixXf : {choixXF}')
            #print(f'phero : {pheromone_rate}')
            #print(best_cellule)


    best_cellule = random.choices(  
        population = choixXF,
        weights = pheromone_rate,
        k=1#longeur de la liste a return 
    )

    return best_cellule[0] # best_cellule est une liste a un tupple, pour rvoyer jsute le tupple -> [0]
        
        
            
#print(think(choix_fourmi, ant_test)) 