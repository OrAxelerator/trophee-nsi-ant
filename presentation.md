# Présentation du projet

### Présentation globale

L'idée de d'origine était de créer une simulation de déplacement des fourmis dans un environnement fermé, et de voir les fourmis trouver le chemin le plus court entre la fourmilière et la nourriture, peu importe la map et sans organisation centrale.

Problématique initiale :
Comment modéliser le comportement de fourmis dans un environnement fermé de manière à faire émerger le chemin le plus court entre une source de nourriture et la fourmilière ?
Plus précisément, comment les fourmis, ne disposant que d’informations locales, peuvent-elles coopérer indirectement pour résoudre un problème d’optimisation ?

L’objectif du projet est de mettre des fourmis dans un environnement fermé (une “carte”), dans laquelle chaque fourmi suit des règles simples comme les déplacements influencés par les phéromones, dépôt de phéromones..
À travers ces interactions locales, le système doit permettre l’émergence d’un comportement global appelé stigmergie, conduisant progressivement à l’identification du chemin le plus court entre la fourmilière et la nourriture, quelle que soit la configuration de la carte.

### Présentation de l'équipe


### Étapes du projet


* **role :**<br>
- Aélys : créer fonction backhome permettant aux fourmis de rentrer vers la fourmilière en s'aidant avec les produits scalaires etc
- Anatole : gérer systeme de path findings A* pour check map
- Axel : site web editeur de map

---

* **création de l'éditeur de map :**<br>
 Le problème était que créer une carte était long et complexe d'où l'idée de créer un éditeur de map en java-script sur une page html  pour pouvoir editer/modifier des cartes et les enregistrer en json, mais cependant si la carte créée dépassait les 30 cases de longeurs l'éditeur ne pouvait pas adpater la taille de la carte affichée. J'ai donc créé un systeme de navigation qui sera réutilisé dans l'affichage de la simulation.

* **problème indexError**<br>
 pour récuperer case de la fourmi 

* **Connexe ?** <br>
 Nous voulions crée de mulitples cartes de différent manières: éditer, création aléatoire, modification.
 Mais il n'y avait pas de sécurité qui assurer que la carte à toujours un chemin entre la fourmillière et la nourritures. Pour répondre a ce problème nous avons créaient une fonction qui regarde toute les cases sans obstacle en partant de la case départ j'usqua la case d'arrivé. Si elle ne découvre plus de nouvelle cases cela montre que la carte n'a pas dessus (pas connexe).


* **modèle témoin**<br>
 nous avons pousser l'idée plus loin la même fonction a pour objectif a donner l un des chemin les plus court. Toujours pareil il découvre les cases accessible en partant de la case départ chaque case découvre de leur point de vue les case possible tour par tour. Donc des que la case ciblée (arrivé) et trouvait nous arrêtons le programme et nous utilisons un autre petit programme retraçons l historique pour seulement avoir une liste indiquant le chemin

* **avancement projet**<br>
 Des améliorations de fonctions ont été crées comme celle de get-cellule quant aux déplacements sur les diagonales possiblement bloquées par des obstacles adjacents, mais n'ayant pas pu résoudre des bugs, nous sommes restés sur une versions ancienne mais sure. D'autres problèmes ont été rencontrés …

* **Conclusion**<br>
Certaines possibilités d'évolutions ont été envisagées : 
 - amélioration de la fonction longer qui présente des problèmes dans les déplacements (opposé)
 - création de plusieurs nourritures sur la carte en fonction de probabilité d'apparition par rapport à l'espace disponible sur la carte
 - ajout de quantité de nourriture qui s'épuise à la suite du passage de fourmis et en fonction d'un nombre aléatoire assez élévé pour continuer à coir apparaître un chemin optimisé de fourmis
 - En second plan, une évolution de l'interface est envisageable sur un plan esthétique mais aussi quant aux options disponibles pour l'utilisateur (gestion vitesse …)
 - possibilité de créer une vision périphérique à la fourmi pour qu'elle puisse tourner sur les cotés si très haut taux de féromones

Ce projet a permis une cohésion d'équipe par une répartition des taches, de l'entraide pour résoudre des problèmes rencontrés, mais aussi nous a permis de mieux maitriser voire apprendre à connaitre certains langages, tout comme il nous a entrainé à élaborer des hypothèses de résolutions de bugs et à les mettre en place avec logique.