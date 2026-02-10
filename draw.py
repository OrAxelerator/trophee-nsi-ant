#from world import espace

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

def draw(list, ant_array):
    for i in range(len(list)):
        for j in range(len(list[0])):
            fourmi = False
            for ant in (ant_array):
                    if ant["pos"][0] == i and ant["pos"][1] == j:
                       fourmi = True
            charctere = list[i][j]
            if list[i][j] == "f":
                charctere = "🌱"
            elif list[i][j] == "X":
                charctere = "🪨"
            elif list[i][j] == "h":
                charctere = "🏠"

            if j == len(list) -1:
                print("🐜" if fourmi else charctere, " ")
            else:
                print(f"{"🐜" if fourmi else charctere}\t",end = " ")
                      
                
#draw(espace)

