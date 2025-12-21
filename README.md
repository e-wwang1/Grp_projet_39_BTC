""
1. Descripion générale du projet
   

Tout d'abord, ce projet a pour objectif de traiter des données expérimentales issues d'une étude sur des souris traitées ou non par un cocktail d'antibiotiques. 
Ensuite, le programme permet de lire un fichier CSV, d'extraire les informations pertinentes (de les analyser dans la partie biologie du projet) ainsi que générer des graphiques pour ainsi visualiser l'évolution de la quantité de bactéries vivantes dans le microbiote intestinal. 


2. Contenu du dépôt
   

Le dépôt contient deux dossiers:
main.py : script principal python permettant de lire le fichier CSV ainsi que générer les graphiques. 
README.md : fichier contenenant les instructions d'utilisations et les limitations du projet. 

3. Instructions pour lancer le programme
   

•  Placer le fichier CSV contenant les données expérimentales dans le même dossier que le fichier main.py.

•  Ouvrir le fichier main.py avec, par exemple Spyder

•  Exécuter le script.

•  Lors de l’exécution, entrer le nom du fichier CSV sans l’extension .csv lorsque le programme le demande.

•  Le programme génère alors un graphique représentant l’évolution des bactéries fécales pour chaque souris et sauvegarde l’image sous le nom out.png.


4. Fonctionnalitées implémentées

•Lecture d'un fichier CSV contenant les données expérimentales 

•détection automatique de toutes les souris présentes 

•Filtrage des données fécales

•Mise en place d'un graphique en ligne représentant l'évolution des bactéries vivantes pour chaque souris

•Différenctiation visuelle des groupes antibiotiques et placebo par un code couleur. 

5. Limitations fonctionnelles


Cependant, ce code présente des limitations:

• le programme n'inclut pas encore de gestion avancée des erreurs (par exemple pour les valeurs incorrectes), ainsi que les valeurs aberrantes et manquantes ne sont pas prises en compte.

• Le programme n'est pas fait pour des fichiers CSV volumineux, en effet, le fichier peut être relu plusieurs fois, ce qui peut ralentir l'exécution pour un grand nombre de données. 

• La structure des fichiers est supposée être toujours identique et correcte à celle fournie (il n'y a aucune vérification automatique du format qui est effectuée).

• Le programme ne permet pas de sélectionner un sous-groupe de souris (par exemple le sexe).

•


6.Conclusion : 


Pour conclure, ce projet permet de manipuler des données expérimentales et de mieux comprendre leur évolution grâce à des graphiques. Même si le programme reste basique et présente certaines limites, il constitue une bonne base pour analyser des données biologiques et pourra être amélioré par la suite avec des fonctionnalités plus avancées.






