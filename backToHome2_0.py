import random
from cellule import get_cellule
from world import espace
from read_world import read_world
from chose2_0 import caclculTaux
from chose2_0 import dico_cases_getCel

turn90 = {(0, -1) : (-1, 0), (-1, 0) : (0, 1), (0, 1) : (1, 0), (1, 0) : (0, -1)}
turnMoins90 = {(0, -1) : (1, 0), (-1, 0) : (0, -1), (0, 1) : (-1, 0), (1, 0) : (0, 1)}

ant1 = { # exemple
    "pos" : [3,1],
    "angle" : (0, 1),
    "have_food" : True
}

anthill1 = {
    "pos" : [0,0]
}

def searchMaxAngle (firstList, underList) :
        max_angle = []
        max_produit_scalaire = [] 
        maxi = underList[0][0] # calcul le produit scalaire le plus élevé
        for el in underList :
            if el[0] > maxi :
                maxi = el[0]

        for el in underList : #regarde si plusieurs produits scalaire max
            if el[0] == maxi :
                max_produit_scalaire.append(el)

        print("max_produit_scalaire", max_produit_scalaire)
        for el in max_produit_scalaire :
            max_angle.append(firstList[el[1]])
        return [max_angle, maxi ]# renvoie les vecteur dans posivector a la position du produit scalaire
    

def maximumFero(choices, ant, anthill, espace, obs): # ANT
    TousRead_world = dico_cases_getCel (choices, ant, espace) 
    # print("aaaaaaaaaaaaaaaaaaaaaa", choices)
    caseEnFonctionFero = caclculTaux(choices, ant, espace, TousRead_world, "case")
    # print("caseEnFonctionFero", caseEnFonctionFero)
    posi_vecteur = meilleurProduitScalaire(choices, ant, anthill, espace, "backHome")
    # print("posi_vecteurposi_vecteur",posi_vecteur)
    if obs == True :
        coef_fero = 30/100
        coef_vecteur = 70/100
    else :
        coef_fero = 10/100
        coef_vecteur = 90/100
         
    if read_world(ant, caseEnFonctionFero, espace) != "f" : 
        valCaseEnFonctionFero = read_world(ant, caseEnFonctionFero, espace) * coef_fero
    else : 
        valCaseEnFonctionFero =1 * coef_fero
    print("val vecteur ", read_world(ant, posi_vecteur, espace))
    if read_world(ant, posi_vecteur, espace) != "f" :
        valVecteur = read_world(ant, posi_vecteur, espace) *coef_vecteur
    else :
        valVecteur = 1 * coef_vecteur
    choix = [posi_vecteur, caseEnFonctionFero]
    print("++++++++++++++", choix, )

    pheromone_rate = [valVecteur, valCaseEnFonctionFero]
    print("++++++++++++++", choix, pheromone_rate)
    best_cellule = random.choices(  
        population = choix,
        weights = pheromone_rate ,
        k=1
    )
    print("WWWWWWWWWWWWWWHHHHH", best_cellule[0])
    return best_cellule[0]


def meilleurProduitScalaire(choix, ant, anthill, espace, mode) :
    
    home_vector = ()
    coordonnee_home = anthill # ou autre selon definition de la position de la fourmillère
    #while ... :
    Xhome_vector = coordonnee_home[1] - ant["pos"][1]
    Yhome_vector = coordonnee_home[0] - ant["pos"][0] 
    home_vector = (Yhome_vector, Xhome_vector)

    res = []
    angles = []
    good_angle = ()
    

    for i, el in enumerate(choix) :
        print("angle regardé", el)
        produit_scalaire = el[0] * home_vector[0] + el[1] * home_vector[1] #calcul vecteur de chaque angle
        print("produit_scalaire 11", produit_scalaire)
        #res.append(produit_scalaire)
        angles.append((produit_scalaire, i)) # stocke le produit scalaire avec la position de l'angle auquel il renvoie
    
    if mode == "produit" :
        print(angles[0][0],"🍇🍇🍇🍇🍇🍇🍇🍇🍇")
        return angles[0][0]

    
    max_angle = searchMaxAngle(choix, angles)[0] #angle possible maximumum p. scalaire
    max_produit_scalaire = searchMaxAngle(choix, angles)[1] #produit scalaire max
    if mode == "backHome" :
        return caclculTaux(max_angle, ant, espace, dico_cases_getCel(max_angle, ant, espace), "vector") 
    
    elif mode == "longer" : ##Calcule le 2eme plus grand p. scalaire
        if len(max_angle) == 2 :
            return max_angle
        else :
            scalaireAngleXmax = []
            
            for el in angles : #[0] p.scalaire [ position dans choix]
                if el[0] != max_produit_scalaire :
                    scalaireAngleXmax.append(el) #[0] p.scalaire [1] position dans choix
            Scalaire2 = searchMaxAngle(choix, scalaireAngleXmax)[0]
            if len(Scalaire2) == 1:
                print(Scalaire2, "🗿🗿")
                return Scalaire2[0]
            else :
                return caclculTaux(Scalaire2, ant, espace, dico_cases_getCel(Scalaire2, ant, espace), "vector") 

def longer(choix, anthill, ant, espace ) :
    v_gauche = turnMoins90[ant["angle"]]#defini les deux possibilités
    v_droite = turn90[ant["angle"]]

    if ant["side"] == 0 :
        fero_left = read_world(ant, v_gauche, espace)
        fero_right = read_world(ant, v_droite, espace)
        if type(fero_left) != int or type(fero_right) != int :
            fero_right = 0
            fero_left = 0

        if fero_left > fero_right:
            ant["side"] = -1 # choisit de longer par la gauche
        elif fero_right > fero_left:
            ant["side"] = 1  #choisit de longer par la droite
        else:
            ant["side"] = random.choice([-1, 1]) # random si pareil
    
    
    case = ""
    compteur = 0

    while case == "" :

        vector1 = ant["angle"]
        if ant["side"] == 1:
            vector2 = turn90[ant["angle"]]
        else:
            vector2 = turnMoins90[ant["angle"]]
        # print(choix, "😍😍😍😍😍😍")
        # print("veeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", vector1, vector2)
        # print(compteur, "❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️")
        if compteur == 100 :
            return "What have u done bro"
        if compteur == 20 :
            ant["side"] = -ant["side"]
            # print("😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈")
    
        if compteur == 40 :
            # print("😈😈😈😈😈😈😈😈😈😈😈😈😈😈😈")
            ant["side"] = -ant["side"]
        etat1 = read_world(ant, vector1, espace)
        etat2 = read_world(ant, vector2, espace)
        # print(etat1,"🗿🗿🗿🗿", etat2, "🤣🤣😶😶😶😗")

        if etat1 == "out" or etat2 =="out" :# si sur une bordure
                ant["angle"] = (-(ant["angle"][0]), -(ant["angle"][1]))

        elif etat2 != "X" and etat1 =="X" : #si v2 libre mais v1 X libre
            if ant["side"] == 1:
                ant["angle"] = turn90[ant["angle"]]
            else :
                ant["angle"] = turnMoins90[ant["angle"]]


        elif etat1 != "X" and etat2 == "X": #si v1 libres et v2 X libre
            message = "NOT GOOD"
            case = vector1

        elif etat1 != "X" and etat2 !="X" :
            produitScalaire = meilleurProduitScalaire([vector1], ant, anthill, espace, "produit" )
            if produitScalaire > 0 :
                ant["mode"] = "home"
                message = "GOOD"
                ant["side"] = 0
                return message
            else :
                if ant["side"] == 1:
                    ant["angle"] = turn90[ant["angle"]]
                else :
                    ant["angle"] = turnMoins90[ant["angle"]]
                message = "NOT GOOD"
                
        elif etat1 == "X" and etat2 == "X" :
            if ant["side"] == 1:
                ant["angle"] = turn90[ant["angle"]]
            else :
                ant["angle"] = turnMoins90[ant["angle"]] 
        compteur+=1
        # print(case, "----------(((((((((((((((((((((((((___________)))))))))))))))))))))))))")
    return (case, message)
        


# def find(posi, ant, obs, anthill): 
#     if obs == True : #si il y a un obstacle alors la fourmi fait en fonction des feros
#         print("///////////////////// 1", posi)
#         choosedOne = maximumFero(posi, ant, anthill, espace) 
#         print("§§§§§§§§§§§§§§§")
       
            
#     elif obs == False :
#         bestAngles = meilleurProduitScalaire(posi, ant, anthill)
#         # if len(bestAngles) == 1 :
#         #     choosedOne = bestAngles
#         # else :
#         #     print("////////////////// 2", bestAngles)
#         #     choosedOne = maximumFero(bestAngles, ant, anthill, espace)
#     return choosedOne

def back_home(ant, anthill, espace, nb_tour) :
    # print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    # while ant["pos"] != anthill["pos"] :
    angle_beginning = ant["angle"]
    # print("----------------------------------------------------------------------------")

        

    # print("Choice angle in process ....")
    choix_angle = [(0,1), (0,-1), (1,0), (-1,0)]
    posi_vector_angle = []
    obs = False
    angleXopposed = []

    for el in choix_angle : #verifie quels angles ont des solutions
        ant["angle"] = el 
        choix = get_cellule(espace, ant, mode = "filtered")
        # print("Choix en cours de reflecion",choix, el)
        choixACx = get_cellule(espace, ant, mode = "all")
        for elm in choixACx :
            if read_world(ant, elm, espace) == "h" : 
                ant["angle"] = angle_beginning
                return elm
            elif read_world(ant, elm, espace) == "X" : 
                obs = True
        if choix != [] :
            posi_vector_angle.append(el)
            if el != (-(angle_beginning[0]), -(angle_beginning[1])) :
                angleXopposed.append(el)
            #regarde si obsatacle autour de la fourmi
    ant["angle"] = angle_beginning
    if ant["mode"] == "longer":
        fonc = longer(choix_angle, anthill, ant, espace)
        print("FFFFFFFFFOOOOOOOOOOOOOOONNNNNNNNNNNCCCCCCCCCC", fonc)
        if type(fonc) == tuple :
            case = fonc[0]
            message = fonc[1]
        else :
            message = fonc #good

        if message == "NOT GOOD":
            print(case)
            return case
        else :
            ant["mode"] = "home"

    if ant["mode"] == "home" :
        print("angle possible vérifiés", posi_vector_angle)
        if nb_tour == 0 :
            possibliyGoodAngle =meilleurProduitScalaire(posi_vector_angle, ant, anthill, espace, "backHome")
        elif nb_tour != 0 :
            verifCoef = False
            possibliyGoodAngle = meilleurProduitScalaire(angleXopposed, ant, anthill, espace, "backHome") # avoir si pas ajouter p. scalaire quand obs
            if possibliyGoodAngle == [] :
                #print("vide")
                possibliyGoodAngle = meilleurProduitScalaire(posi_vector_angle, ant, anthill, espace, "backHome")#avec l'angle opposé
                ant["demi_tour"] = True

            if obs == True :
                coefAngBeginning = 0 if angle_beginning[0] in (-1, 1) else 1
                coefAngPossi = 0 if possibliyGoodAngle[0] in (-1, 1) else 1
                if (coefAngBeginning != coefAngPossi and angle_beginning[coefAngBeginning] == possibliyGoodAngle[coefAngPossi]) == True :
                    verifCoef = True

                if ant["demi_tour"] == True :
                    if verifCoef == True:
                    #3 + calcule
                        ant["demi_tour"] == False
                        v_home = meilleurProduitScalaire(choix_angle, ant, anthill, espace, "backHome")
                        ant["mode"] = "longer" 
                        res = longer(choix_angle, anthill, ant, espace)
                        if type(res) == tuple: # si c'est un mouvement (case, message)
                            return res[0]
                        else: # Si GOOD
                            ant["mode"] = "home"
                        
                    elif verifCoef == False :
                        ant["demi_tour"] == False
                    
                elif ant["demi_tour"] == False: # 1/4
                    if verifCoef == True : # 1
                        ant["demi_tour"] = True
                        
                    elif verifCoef == False: #4
                        pass # 2
        
                    
        print("possibliyGoodAngle", possibliyGoodAngle)
        ant["angle"] = possibliyGoodAngle
        print("Thanks for waiting, angle choosed is ", ant["angle"])
        print("Now, please wait, the choice of direction direction is in process...")
        posi_vector_direction = get_cellule(espace, ant, mode="filtered")
        print("////////////// 3", posi_vector_direction)
        directionChoosed = maximumFero(posi_vector_direction, ant, anthill, espace, obs)
        print("Thanks again, so the ant might go to ", directionChoosed)
            
            #nb_tour += 1
            
        print("POSITION",ant["pos"])
        return directionChoosed

        

#print("test",back_home(ant1, anthill1, espace, 0))

            



    