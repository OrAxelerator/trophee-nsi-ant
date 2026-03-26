from flask import Flask, render_template, Response, request
import time
import json
import os
from load_world import get_map
import random
from cellule import get_cellule
from draw import draw
from read_world import read_world
from chose2_0 import think
from unlock import unblock

from chose_cellule import choose
from backToHome2_0 import back_home
from evap import evaporation
from random_map import random_map
from path import cadjacent, trouve
from  ant import init_ant


app = Flask(__name__)




def move(choix:tuple, ant:dict):
    print("choix de move() : ", choix)
    ant["pos"][0] += choix[0] 
    ant["pos"][1] += choix[1]



def pheromones(espace, ant:dict, pose:int):
    """pose phéromones a la position de la fourmi avant son déplacement
    seulement si elle a de la nourriture"""
    if ant["have_food"]:
        print("pos :", espace[ant["pos"][0]][ant["pos"][1]])
        if espace[ant["pos"][0]][ant["pos"][1]] not in ("f","h") :
            espace[ant["pos"][0]][ant["pos"][1]] += pose


def load_json_list():
    try:
        global json_map
        json_map = os.listdir("static/worlds")
        return json_map
    except Exception as e:
        print(e)
        json_map = []


import os
import json

def ecrire_json(data: dict, nom_fichier: str = "output.json"):
    print("écriture")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dossier = os.path.join(base_dir, "static", "worlds")

    os.makedirs(dossier, exist_ok=True)

    chemin_fichier = os.path.join(dossier, nom_fichier)

    with open(chemin_fichier, "w", encoding="utf-8") as f:#w : écrase a l'écriture si existe déja
        json.dump(data, f, ensure_ascii=False, indent=4)

    return chemin_fichier


path = None
CONFIG = {}


def generer():
    global CONFIG
    global path #chemin le plius cout
    if CONFIG["randomMap"] == True:
        mapdata = random_map(int(CONFIG["y"]), int(CONFIG["x"]), 1.0 - float(CONFIG["pObstacle"]), float(CONFIG["pObstacle"]))
        path = cadjacent(mapdata["map"], mapdata["hill"], mapdata["food"]) 
        while path == None: # Si pas de chemin a food
            mapdata = random_map(int(CONFIG["y"]), int(CONFIG["x"]), 1.0 - float(CONFIG["pObstacle"]), float(CONFIG["pObstacle"])) # recréer map
            path = cadjacent(mapdata["map"], mapdata["hill"], mapdata["food"])  # recalcule si chemin exite
        print("cheeeeeeeeeeeeeeeeck")
        print(path)
        
        #envoyépath en donné static
    else:
        with open(f'static/worlds/{CONFIG["map"]}') as f:
            mapdata = json.load(f)

    print(mapdata)
    hill = mapdata["hill"]
    espace = mapdata["map"]
    print("HIIIIIIIL", hill)
    
    ant_array = init_ant(int(CONFIG["nbAnt"]), hill)
    FOOD = 0
    COEF = 6
    tour = 1
    taux = 0.1
    pose = 100

    while True:
        for ant in ant_array:
            if ant["have_food"]:
                if ant["pos"] != hill:
                    nb_tour = 0 if read_world(ant, (0,0), espace) == "f" else 1
                    seq = [1, 2]
                    num = random.choice(seq)
                    if num == 1 or nb_tour == 0:
                        back_Home = back_home(ant, hill, espace, nb_tour) 
                        case = back_Home
                    else:
                        choix = get_cellule(espace, ant, "filtered")
                        if choix == []:
                            ant["angle"] = unblock(espace, ant)
                        choix = get_cellule(espace, ant, "filtered")
                        case = think(choix, ant, espace, COEF)
                    move(case, ant) 
                    pheromones(espace, ant, pose)
                    if ant["pos"] == hill:
                        FOOD +=1
                        ant["have_food"] = False
                        ant["angle"] = (-(ant["angle"][0]), -(ant["angle"][1]))
            else:
                choix = get_cellule(espace, ant, "filtered")
                if choix == []:
                    ant["angle"] = unblock(espace, ant)
                    choix = get_cellule(espace, ant, "filtered")
                brain = think(choix, ant, espace, COEF)
                move(brain, ant)
        evaporation(espace, taux)
        tour += 1
        data = {
            "ants": ant_array,
            "map": espace,   # prends espace directement
            "food": FOOD,
            "tour": tour
        }

        yield f"data:{json.dumps(data)}\n\n"
        time.sleep(0.2)




@app.route('/')
def index():
    # return render_template('mapedit.html')
    return render_template('index.html', map=load_json_list())

@app.route('/mapedit')
def mapedit():
    return render_template('mapedit.html')  


@app.route("/simulation", methods=['POST'])
def simulation():
    print("=====================")
    global CONFIG
    CONFIG = {
    "map": request.form.get('map'),
    "nbAnt": request.form.get('nbAnt', 5),
    "randomMap": request.form.get('randomMap') == "on",
    "pObstacle": request.form.get('pObstacle', 0),
    "y": request.form.get('y', 10),
    "x": request.form.get('x', 10),
}
    print(CONFIG)
    global path
    print(path)
    return render_template("simulation.html", shortPath=[[0,0], [0, 1], [0, 2]])#, normamentlt config["path"]

@app.route("/stream")
def stream():
    print("STREAM APPELEEEE")
    return Response(generer(), mimetype="text/event-stream")

@app.route("/saveMap", methods=['POST'])
def saveMap():
    data = request.form.get('mapData')
    data = json.loads(data) #convertir en vrai json car js renvoi string
    print(data)
    
    short_path_brut = cadjacent(data["map"], data["hill"])
    if short_path_brut != None:
        short_path = trouve(short_path_brut, data["hill"])
        data["short"] = short_path #rajoute chemin le plus court dans la var "json" data
        print(data["short"])
        ecrire_json(data, data["name"])
    else:
        print("="*20)
        print("⚠️ Map chargé ne contient pas un chemin direct entre la nouritture et la fourmilière ⚠️")
        print("Assurez vous d'avoir mis une source de nourriture et une fourmillière")
        print("="*20)
    
    #save le sjon dans /static/world et rechargé json_map
    # shortPath = cadjacent(data["map"],data["hill"] )  
    #rajouter shortPath a json
    print("YEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEESS")
    
    return render_template('index.html', map=load_json_list())


if __name__ == "__main__":
    app.run(debug=True)