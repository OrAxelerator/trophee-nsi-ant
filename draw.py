from world import espace
from parametre import ant_array

#ant_array = [ { 
#    "pos" : [2, 3],
#    "angle" : (0,1),
#    "have_food" : False
#}, { 
#    "pos" : [3, 3],
#    "angle" : (0,1),
##    "have_food" : False
###    "pos" : [0, 0],
#    "angle" : (0,1),
#    "have_food" : False
#}
#]
def draw(list):
    for i in range(len(list)):
        for j in range(len(list[0])):
            fourmi = False
            for ant in (ant_array):
                    if ant["pos"][0] == i and ant["pos"][1] == j:
                       fourmi = True
            if j == len(list) -1:
                print("🐜" if fourmi else list[i][j], " ")
            else:
                print(f"{"🐜" if fourmi else list[i][j]}\t",end = " ")
                      
                
#draw(espace)

