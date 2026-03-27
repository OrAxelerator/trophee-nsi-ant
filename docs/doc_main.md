### Fonctionnement code :

#### Logique de la simulation :

* Comment sont enregistrées les maps :<br>
Les maps prédéfinies sont enregistrées en json avec plusieur clés : 
    * ``map`` : les données de la map, enregistrées dans une liste contenant plusieurs autres listes enregistrant chacune une ligne : ![](/docs/map_preview.png)
    * ``hill`` : liste contenant les coordonnées de la fourmilière "h".
    * ``chemin_temoin`` : liste contenant toutes les cases du chemin le plus court entre la fourmilière et la nourriture.
    Exemple : ``[[2, 6], [1, 5], [2, 4], [1, 3], [2, 2], "f"]``
    * ``name`` : nom de la map, qui est le même que celui du fichier json.

* Comment est géré l'espace 2d :<br>
Dans la variable ``map`` pour acceder à la case x=4 et y=6 il faut lire à l'indice map[6][4] **les x et y sont inversés dans l'ensemble de ce projet**.

* Comment sont enregistrées les fourmis :<br>
chaque fourmi est un dictionnaire ressemblant à ceci :
    ```python
    {
    "pos" : [0,0], #postion [y,x]
    "angle" :(0,1), 
    "have_food" : False,
    "demi_tour": False,
    "mode" : "home",
    "side" : 0
    }
    ```
    ``angle`` n'a que 4 valeurs possibles :
        ```
        (0,1) : ⭢
        (0,-1) : ⭠
        (1,0) : ⭣
        (-1,0) : ⭡
        ```<br>
        * à noter que les diagonales sont interdites pour les angles.

    Les clés ``demit_tour``, ``mode``, ``side`` sont des clés utilisées par la fonction [``backhome()``](/sources/backToHome2_0.py)

* Les cases : <br>
    |  Case   |     Sens |
    |---    |:-:  
    |   ``int`` >= 1   |   cases libres sur lesquelles les fourmis peuvent marcher   | 
    |   "h" |  Fourmilière  |
    |   "f"   | Nourriture |   

* ``app.py`` :<br>
    * Ce fichier s'occupe de tout connecter, la boucle pricnicpale ``generer()`` et les paramètres de simulation récupérés depuis ``simulation.html``

    * Plusieurs variables comme : le nombre de phéromones déposées, le coef d'attirance des phéromones, le taux d'évaporation des phéromones. Ces 3 varaibles peuvent radicalement changer le cours de la simulation, et selon les maps les valeurs optimales seront différentes.

    * Comment marche l'envoi des donnés de la simulation :
    Toutes les données utiles pour la simulation sont enregistrées dans cette variable : 
        ```python
        data = {
            "ants": ant_array,
            "map": espace,   
            "food": FOOD,
            "tour": tour
            }
        ```
        puis sont envoyées avec
        ```python
        yield f"data:{json.dumps(data)}\n\n"
        ```
        dans [simulation.html](/sources/templates/simulation.html)