from typing import Literal

Case = tuple[int, int]
Valeur = int | Literal['X', 'f', 'h']  # X = obstacle, f = food, h = fourmilière
Espace = list[list[Valeur]]

def update_horizon(pose: tuple[int, int]) -> dict[str, list[int, int]]:
    """
    permet de regarder toute les cases adjacente d'une case ciblée (sert seulement pour cadjacent)
    """
    pos = list(pose)
    return {"haut": [pos[0] - 1,pos[1]],
           "bas": [pos[0] + 1,pos[1]],
           "droite": [pos[0],pos[1] + 1],
           "gauche": [pos[0],pos[1] - 1],
           # rajoute les diagonale
           "haut_gauche": [pos[0] - 1,pos[1] - 1],
           "bas_droite": [pos[0] + 1,pos[1] + 1],
           "haut_droite": [pos[0] - 1,pos[1] + 1],
           "bas_gauche": [pos[0] + 1,pos[1] - 1]}

#trouve le dico qui menne vers le chemin a besoin de uptade horizon pour

def cadjacent (espace: Espace, départ: list[int]) -> None | dict[Case, list[Case]]:
    """
    si on trouve un chemin sans obstacles de départ à arrivée dans espace, on le renvoie sous forme d'un arbre (dictionnaire cellule mère: cellules filles)
    sinon
    """
    L = len(espace[0])
    H = len(espace)
    la = tuple(départ) 
    stockage = {(la): [] }
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
                    elif espace[y][x] == "f":
                        stockage[la].append("f")
                        return stockage
        cb = noeud
   

# fonction qui retrouve le chemin sous forme de liste et renvoie juste la longueur du chemin le plus court 


def trouve (stockage: dict[Case, list[Case]], départ) -> list[Case]:
    """prend en entre la sortie de cadjacent et renvoie la longueur du chemin"""
    viseur = "f"
    chemin: list[Case] = []
    if stockage is None:
        return chemin
    chemin.append(viseur)
    while list(départ) not in chemin:
        for k in stockage:
            if viseur in stockage[k]:
                if tuple(départ) != k: 
                    chemin.append(list(k))
                    viseur = list(k)
                else:
                    chemin.append(list(k))
                    chemin_a_lendroit = []
                    for loop in range(len(chemin)):
                        chemin_a_lendroit.append(chemin[-loop - 1])
                    return chemin_a_lendroit