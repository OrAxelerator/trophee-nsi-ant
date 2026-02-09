espace = [
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, "X", "f", 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
espace1 = [
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, "X", "f", 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0]
]



def update_horizon(pos):
    print("pos:", pos)
    return {"haut": [pos[0] - 1, pos[1]],
           "bas": [pos[0] + 1, pos[1]],
           "droite": [pos[0], pos[1] + 1],
           "gauche": [pos[0], pos[1] - 1]}


def cadjacent(stockage, cb, dimension, espace):
    action = ("haut", "droite", "gauche", "bas")
    noeud = 0
    #global dimension
    #global cb
    #global la
    noeud = 0


    for i in range(cb):
        
        
        la = stockage[len(stockage) - i -1]
        horizon = update_horizon(la)
        print("horizon", horizon)
        for loop in range(4):
            #print("action loop:", action[loop])
            #print("horizon blabla", horizon[action[loop]][0]) # <- -1
            #print("valeur a regarder : ", espace[horizon[action[loop]][0]][horizon[action[loop]][1]])
            #espace[horizon[action[loop]][0]
            
            #if horizon[action[loop]][0] >= 0  and  horizon[action[loop]][0] <= dimension[0] and horizon[action[loop]][1] >= 0  and  horizon[action[loop]][1] <= dimension[1]:
            #regarde si la case existe
            if dimension[0] >= horizon[action[loop]][0] >= 0  and 0 <= horizon[action[loop]][1] <= dimension[1]:
                
                if  espace[horizon[action[loop]][0]][horizon[action[loop]][1]] == 0 and horizon[action[loop]] not in stockage:
                    noeud = noeud + 1
                    #print("horizon loop : ", horizon[action[loop]])
                    # print("horizon: ", horizon)
                    
                
                    stockage.append(horizon[action[loop]])
                    print("stockage", stockage)
                # Si la case "f"
                elif espace[horizon[action[loop]][0]][horizon[action[loop]][1]] == "f":
                    stockage.append("f")
                    print(stockage)
                    return True
                    
    cb = noeud
    if noeud == 0:
        return False


                    
def check_map(map, start:list):
    stockage = [start]
    la = stockage[0] # -> [0,0]
    dimension = [len(map)-1, len(map[0])-1] #compte le zero
    noeud = 0
    cb = 1
    horizon = update_horizon(la)

    while True:
        val = cadjacent(stockage, cb, dimension, map)
        print(val)
        if not val and val != None:
            print("pas de f")
            break

        if val :
            print("ouai")
            break
        
check_map(espace, [0,0])