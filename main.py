import random
from world import espace, LARGEUR, HAUTEUR
from draw import draw

position_fourmi = [0, 6]

action = ("avancer", "droite", "gauche")

def avancer(p):
    return  [p[0] + 1, p[1]]

def droite(p):
    return  [p[0] + 1, p[1] + 1]

def gauche(p):
    return  [p[0] + 1, p[1] - 1]

def pos_ok(p):
    return 0<=p[0]<LARGEUR and 0<=p[1]<HAUTEUR




for loop in range(20):
    choix = random.choice(action)
    if choix == "avancer":
        if pos_ok(avancer(position_fourmi)):
            espace[position_fourmi[0]][position_fourmi[1]] = '👣'
            position_fourmi = avancer(position_fourmi)
    if choix == "droite":
        if pos_ok(droite(position_fourmi)):
            espace[position_fourmi[0]][position_fourmi[1]] = '👣'
            position_fourmi = droite(position_fourmi)
    if choix == "gauche":
        if pos_ok(gauche(position_fourmi)):
            espace[position_fourmi[0]][position_fourmi[1]] = '👣'
            position_fourmi = gauche(position_fourmi)
    espace[position_fourmi[0]][position_fourmi[1]] = '🐜'
    draw(espace)
    print("============")
    input("...")



