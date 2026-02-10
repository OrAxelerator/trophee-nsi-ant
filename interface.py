#from world.random_map import random_map

from draw import draw
from random_map import random_map
map_choosen = []

# while map_choosen != "created" or map_choosen != "random" :
#     map_choosen = input("Do you want to create a random map or an already created one ?  (random/created) : ")
#     if map_choosen == "random" :
#         random_map()
#     elif map_choosen == "created" :
#         map_used = input("Which one do you want to use between : ")

#print(map)
map = random_map(12, 12, 8, 2) #creer
import random
y_h = random.randint(0, 11)
y_x = random.randint(0, 11)
map[y_h][y_x] = "h" # défini "home"
print(y_h,y_x)
from path import check_map

#print(map)
check_map(map, [y_h, y_x]) #determine si map possible a patir de homme
draw(map, []) #affiche