from load_world import get_map
from main import main
from random_map import random_map
from ant import init_ant
from path import cadjacent
from path import trouve
from draw import draw


def start():
    choix_map = input("map aléatoire ou predefini [a/p] : ") or "a"
    if choix_map == "a":
        w = int(input("longeur map : ")) or 10
        h = int(input("hauteur map : ")) or 10
        poidsObstacle = int(input("pourcetage d'obsacle")) or 1
        poidsChemin = int(input("pourcentage")) or 5
        map, hill, food = random_map(x=w, y=h, weightObstacle=poidsObstacle, weightPath=poidsChemin)

        draw(map, [])
        chemin = cadjacent(map, hill, food)

        while chemin == None:
            chemin = cadjacent(map, hill, food)
            print('Problème map - relance création')

        # print("hill", hill)
        mapData = {
            "map" : map,
            "name" : "random_map",
            "hill":(hill[0], hill[1])
        }
        draw(map, [])
    elif choix_map == "p":
        mapData = get_map()

        # chemin = cadjacent(mapData["map"], mapData["hill"], mapData["food"])
        # if chemin == None:
            # print("Map connexe, veuillez reparer la map ou tester une autre")

        # taille_min_chemin = trouve(chemin) # doit tjrs renvoyé un int



    print(mapData)
    nb_ant = int(input("nombre de fourmi : ")) or 2 #Valeur par défault si input == ""
    ant_array =  init_ant(mapData["hill"], nb_ant)

    print(ant_array)
    print(mapData["hill"])

    main(espace=mapData["map"], ant_array=ant_array, hill=mapData["hill"])

if __name__ == "__main__" :
    start()