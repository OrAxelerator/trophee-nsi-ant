from read_world import read_world


ant = { # exemple
    "pos" : (3, 2),
    "angle" : (0,-1),
    "have_food" : True
}

def get_cellule(world, ant: dict, mode:str) -> list:
    """renvoi la liste des positions possibles autour de la fourmi"""
    choices = {
        "up": (-1,0),
        "up-right": (-1,1),
        "up-left": (-1,-1),
        "down" :(1,0),
        "down-right" :(1,1),
        "down-left" :(1,-1),
        "left" :(0,-1),
        "right" : (0,1),
    }

    interdiction=[]
    if ant["pos"][0] == 0:
        interdiction.append(choices["up"])
        interdiction.append(choices["up-right"])
        interdiction.append(choices["up-left"])
    if ant["pos"][0] == len(world[0]) - 1 :
        interdiction.append(choices["down"])
        interdiction.append(choices["down-left"])
        interdiction.append(choices["down-right"])
    if ant["pos"][1] == 0 :
        interdiction.append(choices["left"])
        interdiction.append(choices["down-left"])
        interdiction.append(choices["up-left"])
    if ant["pos"][1] == len(world[0]) - 1:
        interdiction.append(choices["right"])
        interdiction.append(choices["up-right"])
        interdiction.append(choices["down-right"])


    possibility = []
    Read_world = []
    choix = []
    allChoice = []

    for el in choices :
        if choices[el] not in interdiction:
            allChoice.append(choices[el])
            if read_world(ant, choices[el], world) != "X" :
                Read_world.append(read_world(ant, choices[el], world))
                possibility.append(choices[el])
        

    if mode == "all" : 
        return allChoice
    
    elif mode == "filtered" :

        if "f" in Read_world and ant["have_food"] == False :
            return possibility # return toutes les possibilités autour de la fourmi
        
        elif "f" not in Read_world or ant["have_food"] == True :

            coef = 0 # indiceou se situe le 1 ou -1 dans angle
            if ant["angle"][0] == -1 or ant["angle"][0] == 1:
                coef = 0
            elif ant["angle"][1] == -1 or ant["angle"][1] == 1:
                coef = 1

            for el in possibility :
                    if (el[coef] == ant["angle"][coef]):
                            choix.append(el)

            return choix #return par rapport à l'angle
    
   


#print(detectF(espace, ant))
# print(get_cellule(espace, ant, mode = "all")) #test``


# ---------------
#CODE PAS ENCORE STABLE

# from world import espace
# from read_world import read_world

# ant = { # exemple
#     "pos" : [0,0],
#     "angle" : [0,1],
#     "have_food" : False
# }

# def get_cellule(world, ant: dict) -> list:
#     """renvoi la liste des positions possibles autour de la fourmi"""
#     # tout en empechant case impossibe car bloqué entre 2 espace
#     dir_ilegal = [] # angle ilegal (qui amene en dehors de map)
#     if ant["pos"][0] == 0:
#         dir_ilegal.append([-1,0])
#     if ant["pos"][0] == len(world[0]) - 1 :
#         dir_ilegal.append([1,0])
#     if ant["pos"][1] == 0 :
#         dir_ilegal.append([0,-1])
#     if ant["pos"][1] == len(world[0]) - 1:
#         dir_ilegal.append([0,1])


#     if ant["have_food"]:
#         angle = ant['angle']
#     else:
#         ANGLE = [[1,0], [-1,0], [0,1], [0,-1]]
#         angle = [a for a in ANGLE if a not in dir_ilegal]
#         print("nalge",angle)    
#     # si ant a de la nourriture on check tout les angles sinon on check que sont angle
#     case = [] # toute les case légal (dans map est != "X")

    
#     for dir in angle: # pour le nombre de dir simple legal (H,B,G,D)
#             print("-----------------------------------")
#             print("dir simple check", dir) # tout les dir simple legal
#             coef = 1 #si if : FAlse else coef = 1
#             if dir[0] == -1 or dir[0] == 1:
#                 coef = 0   # sur quel index se trouve le 1 ou -1 car sur dir de base il peut y avoir que un (1/-1) et un 0
#                 # avec le coef on peut lire dir[coef] pour "savoir direction"
#                 #il suffit que dir_random[coef] == dir[coef] pour certififé que dir_random fait parti des 2 autre direction de dir
#                 #EX : si dir represente "droite" alros case_random[1-coef] = -1 = haut droite etcase_random[1-coef] = haut bas
#                 # ( avec dir_random[coef] == dir[coef] )
#             print("coef", coef)
#             if read_world(ant, dir, espace) != "X":
#                 case.append(dir) # else don't append
#                 # append (dir : angle "simple")
#             angle_diagonal = (1, -1)
#             for diagonal in angle_diagonal:
#                 test_ang = [0,0] # diagonal
#                 test_ang[1 - coef] = diagonal # puis -1
#                 test_ang[coef] = 0 # change pas
#                 a = [0,0]
#                 a[coef] = dir[coef]
#                 a[1 - coef] = test_ang[1 - coef]
                
#                 if test_ang not in dir_ilegal and a not in case:
#                     print("test ang : ", test_ang)
#                     print(read_world(ant, dir, espace))
#                     print(read_world(ant, test_ang, espace))
#                     if read_world(ant, a, espace) != "X": # check d'abord valeur de diagonal et rajoute que si une des 2 case adj et != "X"
#                         if read_world(ant, dir, espace) == "X" and read_world(ant, test_ang, espace) == "X": # test du 1 d'abord
#                             print("case diag bloqué : ", (dir[coef], 1))
#                         else:
#                             print("case diag accessible : ", a) # append a choix_360 
#                             print("case ava:", case)
#                             print(a in case)
#                             case.append(a)
#                             #d'abord lire val car si "X":bloqué
#                             # d'abbord check si diagonal = "X" car plus opti


#     print("fin ode coef -----------------------")
#     print("dir ilegal", dir_ilegal)
#     print("chemin legal", case) # 360

# get_cellule(espace, ant) # problème la va dire 2 fois que (1,1) est dispo : mal opti
#  #comment faire en sorte que cherche pas plusieur fois meme diag