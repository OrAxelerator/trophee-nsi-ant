import json
import os

def get_map() -> dict:
    """affiche toute les maps dans /worlds et en fonction de input de l'utilisateur return le fichier json de la map voulu par l'utilisateur en dictionnaire'"""
    json_map :list = os.listdir("static")
    for i, map in enumerate(json_map):
        print(f"{i} - {map}")

    num = int(input(f"quel map prendre :  [0-{len(json_map) - 1}] "))
    name =json_map[num] 
    with open(f'static/{name}') as f:
        d = json.load(f)
    return d