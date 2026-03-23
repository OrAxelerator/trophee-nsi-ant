from world import espace
from draw import draw
#import time


def evaporation(world, taux):  
    for y in range(len(world)):
        for x in range(len(world[y])):

            if type(world[y][x]) == int and world[y][x] > 0:
                
                
                world[y][x] = int(world[y][x] * (1 - taux))

               
                if world[y][x] < 1:
                    world[y][x] = 1
                    #return




    #time.sleep(0.1)

#evaporation(espace, 0.05)   # 5% d'évaporation par tick
#draw(espace, [])