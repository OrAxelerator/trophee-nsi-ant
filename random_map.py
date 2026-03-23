import random

def random_map(y:int, x:int, weightPath:float, weightObstacle:float) :
    """
    Docstring pour random_map
    :param y: hatuer de la map
    :param x: longeur de la map
    :param weightPath: pourcentage de case type obstacle
    :param weightObstacle: pourcentage de case type phéromone
    """
    choix = [1,"X"]
    espace = []
    height = x
    width = y

    for i in range(height):
        row = []
        for _ in range(width):
            ch = random.choices(
                population=choix,
                weights=[weightPath, weightObstacle],
                k=1
                )
            row.append(ch[0])
            
        espace.append(row)
    # position y/x de food    
    yF, xF = random.randint(0, height-1), random.randint(0, width-1)
    espace[random.randint(0, height-1)][random.randint(0, width-1)] = "f"
    # position y/x de Hill
    yH, xH = random.randint(0, height-1), random.randint(0, width-1)
    while (yF, xF) == (yH, xH): # evite que hill soit sur food
        yH, xH = random.randint(0, height-1), random.randint(0, width-1)
        
    espace[yH][xH] = "h"

    return espace, (yH, xH), (yF, xF)


