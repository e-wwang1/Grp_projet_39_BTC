""
1. Descripion générale du projet 

Tout d'abord, ce projet à pour objectif de traiter des données expérimentales issues d'une étude sur des souris traitées ou non par un cocktail d'antibiotiques. 
Ensuite, le programme permet de lire un fichier CSV, d'extraire les informations pertinentes (de les analyser dans la partie biologie du projet) ainsi que générer des graphiques pour ainsi visualiser l'évolution de la quantité de bactéries vivantes dans le microbiote intestinale. 


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


5. Fonctionnalitées implémentées

•Lecture d'un fichier CSV contenant les données expérimentales 
•détection automatique de toutes les souris présentes 
•Filtrage des données fécale
•Mise en place d'un graphique en lignes représentant l'évolution des bactéries vivantes pour chaque souris
•Différenctiation visuelle des groupes antibiotiques et placebo par un code couleur. 

6. Limitations fonctionnelles 
Cependant, ce code présente des limitations : certaines fonctionnalitées demandées dans les consignes ne sont pas encore implémentées ou du moins elles le sont mais partiellement:
• le programme n'inclut pas encore de gestion avancée des erreurs (par exemple pour les valeurs incorrectes), ainsi les valeurs aberrantes et manquantes ne sont pas prises en compte
• Le programme n'est pas fait poyr des fichiers CSV volumineux
• La structure des fichiers sont supposés être toujours identiques et correctes à celle fournie






