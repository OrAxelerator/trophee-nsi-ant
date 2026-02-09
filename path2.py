espace = [#for test
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "f"]
]
espace_0 = [#for test
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, "X", "f"], 
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, "X", 0],
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, "X"], 
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, "X", "X"], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
espace1 = [#for test
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, "f"], 
    [0, 0, 0, 0, "f", 0, 0, 0, 0, 0, 0, 0],
    ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"], 
    [0, "X", "X", 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, "X", "X", 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, "X", "X", 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, "X", "X", 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, "X", "X", 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, "X", "X", 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, "X", "X", 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, "X", "X", 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
espace2 = [#for test
    [0, 0, "X", 0, 0, 0, 0, 0, 0, 0, "X", "f"], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["X", "X", "X", 0, "X", "X", 0, 0, 0, 0, 0, 0], 
    [0, "X", "X", 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, "X", "X", 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, "X", "X", 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, "X", "X", 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, "X", "X", 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, "X", "X", 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, "X", "X", 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["X", "X", "X", 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, "X", 0, 0, 0, 0, 0, 0, 0]
]




def update_horizon(pos):
    #print("pos:", pos)
    return {"haut": [pos[0] - 1, pos[1]],
           "bas": [pos[0] + 1, pos[1]],
           "droite": [pos[0], pos[1] + 1],
           "gauche": [pos[0], pos[1] - 1]
           }


stockage = []
def update_stockage(arg):
    if arg == "get":
        return stockage
    else:
        stockage.append(arg)


def cadjacent(stockage, cb, dimension, espace):
    action = ["bas", "droite", "gauche", "haut"]
    noeud = 0


    for i in range(cb+1):
        print("i : -------------------------------", i)
        print("CB : -------------------------------", cb)
        la = stockage[len(stockage) - i -1]
        horizon = update_horizon(la)
        #print("horizon", horizon)
        for loop in range(4):
            print("loop;",loop)
            #regarde si la case existe
                # Si la case "f"
            if dimension[0] >= horizon[action[loop]][0] >= 0  and 0 <= horizon[action[loop]][1] <= dimension[1]:
                if espace[horizon[action[loop]][0]][horizon[action[loop]][1]] == "f":
                    update_stockage("f")
                    #print(stockage)
                    print("CORD : ",horizon[action[loop]][0])
                    print("CORD : ",horizon[action[loop]][1])
                    return True
                
                elif  espace[horizon[action[loop]][0]][horizon[action[loop]][1]] == 0 and horizon[action[loop]] not in stockage:
                    noeud += 1
                    print(noeud)
                    #print("horizon loop : ", horizon[action[loop]])
                    # print("horizon: ", horizon)
                    
                
                    update_stockage(horizon[action[loop]])
                    print(f"ADD : {action[loop]}")
                    print("S = ",stockage)
                    
                    #print("stockage", stockage) 
    
    cb = noeud# modifié dynamiquement bug ...

    
    if noeud == 0:
        return False
    else:
        print("----------")
        print(f"{noeud} NEW CASE")
        return noeud


                    
def check_map(map:list, start:list):
    
    update_stockage(start)
    la = stockage[0] # -> [0,0]
    print("la :",la)
    dimension = [len(map)-1, len(map[0])-1] #compte le zero
    print("DIMENSION:",dimension)
    noeud = 0
    cb = 1
    horizon = update_horizon(la)
    print("hfdrfioshrifumoeuvç sqfym eiofvioezyqbcfoiefoimqyoqiomqcqyzeciomqiz")
    while True:
        val = cadjacent(update_stockage("get"), cb, dimension, map)
        if type(val) == int:
            print("val = cb",val)
            cb = val
        #print("stock : ",update_stockage("get"))
        #print(val)

        if val == True and type(val) == bool:
            print(stockage)
            print("TROUVÉ ---------------------------")
            return True
            break

        if   val == False :
            print(update_stockage("get"))
            print("noooooo")
            if [0, 11] in stockage:#pos de f
                print("Bug")
            return False
            
        
print(check_map(espace_0, [0,0]))#test
from draw import draw
draw(espace_0, [])
