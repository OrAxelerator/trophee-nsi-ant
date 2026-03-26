

from read_world import read_world



def get_cellule(world, ant: dict, mode: str) -> list:
    """renvoi la liste des positions possibles autour de la fourmi"""
    # tout en empechant case impossibe car bloqué entre 2 espace
    dir_ilegal = [] # angle ilegal (qui amene en dehors de map)
    if ant["pos"][0] == 0:
        dir_ilegal.append([-1,0])
    if ant["pos"][0] == len(world) - 1 :
        dir_ilegal.append([1,0])
    if ant["pos"][1] == 0 :
        dir_ilegal.append([0,-1])
    if ant["pos"][1] == len(world[0]) - 1:
        dir_ilegal.append([0,1])


    if mode == "filtered" :
        angle = [ant['angle']] # les 3 angles
        print("angle", angle)
    elif mode == "almostAll" or mode == "all": 
        ANGLE = [[1,0], [-1,0], [0,1], [0,-1]]
        angle = [a for a in ANGLE if a not in dir_ilegal]
        print("nalge",angle)    
    # si ant a de la nourriture on check tout les angles sinon on check que sont angle
    case = [] # toute les case légal (dans map est != "X")

    
    for dir in angle: # pour le nombre de dir simple legal (H,B,G,D)
            print("-----------------------------------")
            print("dir simple check", dir) # tout les dir simple legal
            coef = 1 #si if : FAlse else coef = 1
            print("dor&", dir)
            if dir[0] == -1 or dir[0] == 1:
                coef = 0   # sur quel index se trouve le 1 ou -1 car sur dir de base il peut y avoir que un (1/-1) et un 0
                # avec le coef on peut lire dir[coef] pour "savoir direction"
                #il suffit que dir_random[coef] == dir[coef] pour certififé que dir_random fait parti des 2 autre direction de dir
                #EX : si dir represente "droite" alros case_random[1-coef] = -1 = haut droite etcase_random[1-coef] = haut bas
                # ( avec dir_random[coef] == dir[coef] )
            print("coef", coef)
            if mode == "almostAll" or mode == "filtered":
                if read_world(ant, dir, world) != "X":
                    case.append(tuple(dir)) # else don't append
                    # append (dir : angle "simple")
            elif mode == "all" :
                case.append(tuple(dir))
            angle_diagonal = (1, -1)
            for diagonal in angle_diagonal:
                test_ang = [0,0] # diagonal
                test_ang[1 - coef] = diagonal # puis -1
                test_ang[coef] = 0 # change pas
                a = [0,0]
                a[coef] = dir[coef]
                a[1 - coef] = test_ang[1 - coef]
                
                if test_ang not in dir_ilegal and tuple(a) not in case :
                    print("test ang : ", test_ang)
                    print(read_world(ant, dir, world))
                    print(read_world(ant, test_ang, world))
                    if mode == "almostAll" or mode == "filtered":
                        if read_world(ant, a, world) != "X": # check d'abord valeur de diagonal et rajoute que si une des 2 case adj et != "X"
                            if read_world(ant, dir, world) == "X" and read_world(ant, test_ang, world) == "X": # test du 1 d'abord
                                print("case diag bloqué : ", (dir[coef], 1))
                            else:
                                print("case diag accessible : ", a) # append a choix_360 
                                print("case ava:", case)
                                print(a in case)
                                case.append(tuple(a))
                                #d'abord lire val car si "X":bloqué
                                # d'abbord check si diagonal = "X" car plus opti
                    elif mode == "all" :
                        case.append(tuple(a))
    print("CAAAAASSSEEE", case)
    return case


# print(get_cellule(world, ant1, "filtered")) # problème la va dire 2 fois que (1,1) est dispo : mal opti
 #comment faire en sorte que cherche pas plusieur fois meme diag
