import os  # Pour récupérer la taille du terminal
from world import espace  # Importer le tableau de jeu

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


# ant_array = [
#     {"pos": [0, 0], "angle": (0,1), "have_food": False},
#     {"pos": [4, 3], "angle": (0,1), "have_food": False}
# ]

def draw(list, ant_array):
    # Parcourt chaque ligne
    for i in range(len(list)):
        # Parcourt chaque colonne
        for j in range(len(list[0])):
            fourmi = False  # Variable pour savoir s'il y a une fourmi ici
            # Vérifie chaque fourmi
            for ant in ant_array:
                if ant["pos"][0] == i and ant["pos"][1] == j:
                    fourmi = True  # La cellule contient une fourmi
                    ch = "🚗" if ant["have_food"] else  "🐜"

            # Récupère le contenu de la cellule
            charctere = list[i][j]

            # Remplace les codes par des icônes
            if list[i][j] == "f":
                charctere = "🌱"  # Nourriture
            elif list[i][j] == "X":
                charctere = "🪨"  # Pierre
            elif list[i][j] == "h":
                charctere = "🏠"  # Maison

            # Affichage
            if j == len(list[0]) - 1:  # Si c'est la dernière colonne

                print(ch if fourmi else charctere)  # Saut de ligne après
            else:
                # Affiche avec tabulation entre les colonnes
                print(f"{ch if fourmi else charctere}\t", end="")

# # Récupère la taille du terminal
# size = os.get_terminal_size()
# columns = size.columns
# lines = size.lines

# # Calcul de la largeur maximale de chaque colonne
# nb_colonnes = len(espace[0])
# largeurs_colonnes = [0] * nb_colonnes

# for ligne in espace:
#     for i, cellule in enumerate(ligne):
#         # Convertit en string pour mesurer correctement les emojis et int
#         largeurs_colonnes[i] = max(largeurs_colonnes[i], len(str(cellule)))

# # Affichage centré du tableau
# for ligne in espace:
#     # Formate chaque cellule selon la largeur max de la colonne
#     ligne_formatee = "        ".join(str(cellule).ljust(largeurs_colonnes[i])
#                                      for i, cellule in enumerate(ligne))
#     # Centre la ligne horizontalement dans le terminal
#     print(ligne_formatee.center(columns))

# draw(espace, [])
# print(f"Largeur : {columns}, Hauteur : {lines}")
# print(len(espace)*7.33 + 1)
