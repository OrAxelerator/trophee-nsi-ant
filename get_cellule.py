from main import espace
ant1 = (0,0)


def get_cellule(world, tuple):
    choices = {
        "droite" : (0,1),
        "bas" :(-1,0),
        "gauche" :(0,-1),
        "haut": (1,0)
        }
    
    res=[]
    if tuple[0] == 0: # 
        res.append(choices["haut"])
        pass 
    elif tuple[0] == len(world[0]) - 1 :
        res.appen(choices[ "bas"])
        pass 
    elif tuple[1] == 0 :
        res.append(choices["gauche"])
        pass 
    elif tuple[1] == len(world[0]) - 1:
        res.append(choices["droite"])
        pass 

    possibilite = []
    for el in res :
        print(el)
        if el not in choices:
            print("recup")
            possibilite.append(el)
        
    print("res : ", possibilite)






get_cellule(espace,ant1 )