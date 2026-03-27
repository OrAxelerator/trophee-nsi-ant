### Et l'ia ?

Dans ce projet l'ia a été très peu utilsisée  sauf dans les cas suivants :


* **Architecture flask** : personne dans le groupe ne connaissait le module python Flask. Le prof nous a montré comment renvoyer une variable python dans une variable java-script mais cette méthode nécéssite le rechargement de la page alors l'ia a trouvé une architecture qui permet d'envoyer en continu un flux de données sans recharger la page html. 

> fichier touché : app.py & templates/simulation.html

* Gestion des listeners : problème de listeners dans le code de l'éditeur de map et du système de navigation. Les listeners s'accumulaient et causaient des bugs, 
le système de navigation et la transformation de l'état des cases dans l'éditeur est donc fait par ia. et aussi de la fonction qui bloque requette du ```<form>```pour attendre que utilisateur rentre nom de la map est soit rajouter dans .value d'une div invisible.
> fichier touché : static/editor/mapedit.js & templates/simulation.html

