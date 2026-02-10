from cellule import get_cellule
from world import espace
from read_world import read_world


ant1 = {
    "pos" : [0,11],
    "angle" : (1,0),
    "have_food": False
}

def unblock(espace, ant):
    Choix = []
    res = [] # toute les angles possible sauf "demi tour"
    ang = [1,-1]
    #possie = []
    angleOpposed = (-(ant["angle"][0]), -(ant["angle"][1]))
    angle_before = ant["angle"]
    print("angle op", angleOpposed)
    for el in ang : 
        #print("angle for :", (el, 0))
        ant["angle"] = (el, 0)
        print("angle1",(el, 0))
        print("get-cel : ", get_cellule(espace, ant))
        if get_cellule(espace, ant) != [] and ant["angle"] != angleOpposed :
            for i in range(len(get_cellule(espace, ant))) :
                if abs(get_cellule(espace, ant)[i][0]) != abs(get_cellule(espace, ant)[i][1]) :
                    print("get-cel : ", get_cellule(espace, ant))
                    res.append((el, 0))
                    print("passage")

    for el in ang :
        #print("angle for :", (0,el))
        ant["angle"] = (0, el)
        print("angle2",(0, el))
        
        if get_cellule(espace, ant) != [] and ant["angle"] != angleOpposed :
            for i in range(len(get_cellule(espace, ant))) :
                if abs(get_cellule(espace, ant)[i][0]) != abs(get_cellule(espace, ant)[i][1]) :
                    print("get-cel : ", get_cellule(espace, ant))
                    res.append((0, el))
                    print("res", res)
                    print("passage")
    
    if res == []:
        print("demi-tour")
        return (-(angle_before[0]), -(angle_before[1]))
            
    print("res: ", res)
    phero = []
    for i, el in enumerate(res) : #
        #ant["angle"] = el
        #Choix = get_cellule(espace, ant)
        #phero.append((ant["pos"], (el))
        val = read_world(ant, el)
        if val == "X":
            pass
        else:
            phero.append(val)

    print("phero : ", phero)
    angle = res[phero.index(max(phero))]
    print("res de la mort, ",angle)
    return angle
        
        #print("+1 dans possi")
       # possie.append((think2(Choix, ant), ant["angle"])) # ((choix[0][0], poids[0][1]), angle[1])
    #maxi = [] 
    # good_one = []
    # maxi = possie[0][0][1]
    # print("maxi anvant for", maxi)
    # print(possie)
    # for el in possie :
    #     if len(el[0]) == 1 : # "f" présent
    #         return el[1] 
    #     elif len(el[0]) == 2 : # pas de "f"
    #          # 
    #         print("maxi : ",maxi)
    #         if maxi < el[0][1]:
    #             good_one = el[1]
    #             print("maxi-2 : ",maxi)

    #             if maxi:
    #                 pass

    # print("Good one :",good_one)
    # return good_one

    
print(unblock(espace, ant1))