# permet de regarder toute les cases adjacente d'une case ciblée (sert seulement pour cadjacent)

def update_horizon(pose):
    pos = list(pose)
    return {"haut": [pos[0] - 1,pos[1]],
           "bas": [pos[0] + 1,pos[1]],
           "droite": [pos[0],pos[1] + 1],
           "gauche": [pos[0],pos[1] - 1]}

#trouve le dico qui menne vers le chemin a besoin de uptade horizon pour marcher

def cadjacent (espace, départ, arrivée) -> None | dict:
    """
    si on trouve un chemin sans obstacles de départ à arrivée dans espace, on le renvoie sous forme d'un arbre (dictionnaire cellule mère: cellules filles)
    sinon
    """
    L = len(espace[0])
    H = len(espace)
    stockage = {(0,0): [] }
    la = (0,0) 
    horizon = update_horizon(la)
    noeud = 0 # le nombre de case trouvées
    cb = 1 # le nombre de nouvelle case a analyser
    while "f" not in stockage:
        noeud = 0
        if cb == 0:
            break
        for i in range(cb):
            autour = 0       
            la = list(stockage.keys())[-1 -noeud -i] 
            horizon = update_horizon(la)
            for k in horizon:
                y, x = horizon[k]            
                if 0<= x < L and 0<= y < H: # la case est dans le monde
                    if espace[y][x] == 1: # la case est libre
                        if not tuple([y, x]) in stockage:
                            stockage[la].append([y, x])
                            stockage[tuple([y, x])] = []
                            noeud += 1
                    # Si la case "chemin"
                    elif espace[y][x] == "f":
                        stockage[la].append("f")
                        return stockage
        cb = noeud
   

sp = [
    ["D", 0, 0, 2, "A"],
    [0, 0, 0, 2, 0],
    [0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0]
]

a = [0, 4]
d = [0, 0]                    

# sto = cadjacent(sp, a, d)
# print(sto)



# fonction qui retrouve le chemin sous forme de liste et renvoie juste la longueur du chemin le plus court 


def trouve (stockage):

    """prend en entre la sortie de cadjacent et renvoie la longueur du chemin"""
 
    


    viseur = "A"
    chemin = []

    chemin.append(viseur)

    

    while "D" not in chemin:
        for k in stockage:
            if viseur in stockage[k]:
                if "D" != k: 
                    chemin.append(list(k))
                    viseur = list(k)
                else:
                    chemin.append(k)
                    chemin_a_lendroit = []
                    for loop in range(len(chemin)):
                        chemin_a_lendroit.append(chemin[-loop - 1])

                    return len(chemin_a_lendroit)