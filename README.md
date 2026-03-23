# Trophee-NSI-ant

### Pour commencer
Ce projet vise à simuler les `déplacements` des fourmies d'une colonie pour trouver leur ``nourriture`` par le biais de ``phéromones`` laissées sur leur passage.

### Instalation
```
git clone https://github.com/OrAxelerator/trophee_nsi_ant.git
```

### Démarrage :
Pour lancer le projet il faut allez dans le dossier ``trophee_nsi_ant``
```
cd trophee_nsi_ant
```
et installez la librairie ``colorama``
```
pip install -r requirements.txt 
```
et executé  le ficher ``python`` init.py

### Fabriqer avec :
* python (pour la logique) et libraire colorama
* html, css, js (pour le [site](https://oraxelerator.github.io/trophee_nsi_ant/tools/index.html))
* json (pour les maps)




### License 
Le projet est sous license **GNU** - voir le fichier [LICENSE](/LICENSE.md) pour plus d'informations.




---








Ce projet vise à simuler les `déplacements` des fourmies d'une colonie pour trouver leur ``nourriture`` par le biais de ``phéromones`` laissées sur leur passage.

On retrouve différents ``fichiers sources`` :
- [``main``](main.py) : le fichier d'entrée du programme
- [``get-cellule``](cellule.py): permettant de voir les possibilités de déplacement d'une fourmi
- [``draw``](draw.py) : permettant un affichage épuré
- [``move``](main.py) : fichier qui simule les déplacements aléatoires des fourmies sur la map choisie
- [``food``](food.py) : avec juste la position d'une fourmi et ces déplacement possible elle detecte si elle à accès a de la nourriture ("f")

## Processus de la simulation 
Vous disposez de `plusieurs maps `monde à votre guise, à vous de choisir celle qui vous convient selon leur `typographie` que ce soit par rapports aux obstacles qu'elle présente, la taille de la carte etc... 

Les fourmies commencent la simulation en sortant de leur fourmilière. Elles ont alors la possiblité des créer des chemins pour 

---

Créer votre propre map depuis ce site : 
https://oraxelerator.github.io/trophee-nsi-ant/tools/index.html
