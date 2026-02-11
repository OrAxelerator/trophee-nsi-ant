from cellule import get_cellule 
import random
from world import espace
from cellule import get_cellule
#from ..world import espace
from read_world import read_world

ant_test = {
      "pos" : [4,2],
      "angle" : (1,0),
      "have_food" : False
}
choix_fourmi = get_cellule(espace, ant_test)

def think(choix: list, ant: dict, espace:list) -> tuple: 

    """
    renvoi le chemin le 'plus optimisé' selon les phéromones
    si la fourmi n'as pas accés a de la nourriture.
    Sinon renvoi le chemin direct a la nourriture si il y en a
    """
    food_path = []
    pheromone_rate1 = []
    pheromone_rate = []
    #choixXF = []
    #TtChoix =[]
    TousRead_world = {}
    #print("choix : " , choix)
    print("choaaaaaaaa : " , choix)
    print("ANGLE", ant["angle"])
    for el in choix :
        print("ELLL", el)
        print("READ", read_world(ant, el, espace))
        TousRead_world[read_world(ant, el, espace)] = 0
    print("TousreadWorld 2", TousRead_world)
    
    for el in choix :
            TousRead_world[read_world(ant, el, espace)] += 1 #compte le nombre de f il y a (si il y en a)
            print("choix choix el ", TousRead_world)

    print("read_world :",TousRead_world)
        
    if "f" not in TousRead_world : #si il n'y a pas de f autour de la fourmi
        for el in choix : 
            #choixXF.append(el) #recupere les choix de la fourmi sans f
            #print("choixXF : ",choixXF)
            #print("el-ajouté")
            pheromone_rate.append(read_world(ant, el, espace) / len(choix)) #fais le poids de chaque possiblité
            
            #print("-----")
            #print(f'choixXf : {choixXF}')
            #print(f'phero : {pheromone_rate}')
            #print(best_cellule)


        best_cellule = random.choices(  
            population = choix, #choixXF
            weights = pheromone_rate,
            k=1#longeur de la liste a return 
        )
        #print("xF")
        #print("best", best_cellule)

        return best_cellule[0] # best_cellule est une liste a un tupple, pour rvoyer jsute le tupple -> [0]

        
    elif "f" in TousRead_world : # si il y a un f autour de la fourmi
        if ant["have_food"] == False: # si elle a deja de la nourriture 
            for el in choix :
                #print("read_world",read_world(ant, el))
                if read_world(ant,el, espace) == "f" :
                    food_path.append(el) # récupere les emplacements de f
            #ant["angle"] = (-(ant["angle"][0]), -(ant["angle"][1])) #si sur food, prend direction inverse
            #print("Food Food Food")
            ant["have_food"] = True # dis qu'elle a à present de la nourriture
            #print("f/false")
            return random.choice(food_path) # choisi random un f autour de la fourmi si il y en a plusieurs

        elif ant["have_food"] == True : #si elle avait deja de la nourriture
                #print("TTchoix:",TtChoix)
            for el in choix :
                if read_world(ant, el, espace) != "f" :
                    pheromone_rate1.append(read_world(ant, el, espace) / len(choix)) #calcule le poids des cases
                    print("DONE")
                #print("pheromone_rate1", pheromone_rate1)
            
            
            for k in range(TousRead_world["f"]) :
                pheromone_rate1.append(1 / len(choix))  # ajoute un poids avec pour 1 feromone pour chaque f 
                
            
            print("pherromone",pheromone_rate1)
            print("CHOIX", choix)
            best_cellule1 = random.choices(  
                population = choix,
                weights = pheromone_rate1,
                k=1
            )
            #print("bestie", best_cellule1)

            #print("f/True")
            return best_cellule1[0]
        
        
            
print("think :",think(choix_fourmi, ant_test, espace)) 