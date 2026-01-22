from get_cellule import get_cellule
from main import espace

# entré : get_cellule()

# sortie la cas avec de la nourriture "f"
ant1 = (0,0) # y, x
ant2 = (4,11)
ant3 = (11,11)

possi = get_cellule(espace, ant1)

print(possi)
def food(possibility, ant):
    for choix in possibility :   
        print(choix)
        print(espace[ant[0] + choix[0] ])
        y = ant[0] + choix[0] 
        x = ant[1] + choix[1]

        if espace[y][x] == "f":
             #ant1 = ( ant1[0] + possibility[0[0]], ant1[1] + possibility[0[1]] )
             print("azertyuiop^qsdfghjklmwxcvbn")
        return True 


food(possi, ant1)