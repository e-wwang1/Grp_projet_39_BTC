

1. Descripion générale du projet



Tout d'abord, ce projet a pour objectif de traiter des données expérimentales issues d'une étude sur des souris traitées ou non par un cocktail d'antibiotiques. 
Ensuite, le programme permet de lire un fichier CSV, d'extraire les informations pertinentes (de les analyser dans la partie biologie du projet) ainsi que générer des graphiques pour ainsi visualiser l'évolution de la quantité de bactéries vivantes dans le microbiote intestinal. 


2. Contenu du dépôt


   
Le dépôt contient deux dossiers:

• main.py : script principal python permettant de lire le fichier CSV ainsi que générer les graphiques. 

• README.md : fichier contenenant les instructions d'utilisations et les limitations du projet. 

Lors de l’exécution du script, trois dossiers supplémentaires sont automatiquement créés afin d’organiser les données :
un dossier input, contenant le fichier CSV utilisé pour l’analyse, un dossier images, contenant les graphiques générés par le programme et enfin un dossier output, regroupant les fichiers CSV des résultats extraits à partir des données initiales.


3. Instructions pour lancer le programme


   
Pour exécuter le programme suivre les instructions suivantes :
•  Placer le fichier CSV contenant les données expérimentales dans le même dossier que le fichier main.py.

•  Ouvrir le fichier main.py avec, par exemple Spyder

•  Exécuter le script

•  Lors de l’exécution, entrer le nom du fichier CSV sans l’extension .csv lorsque le programme le demande

Le programme copie alors automatiquement ce fichier dans le dossier input, traite les données qu’il contient et génère les résultats sous forme de graphiques et de fichiers CSV.


4. Fonctionnalitées implémentées



Tout d'abord,le programme implémente plusieurs fonctionnalités permettant l’analyse des données expérimentales. Il est capable de lire un fichier CSV contenant les résultats bruts de l’étude et de détecter automatiquement l’ensemble des souris, sans intervention manuelle de l’utilisateur.
Ensuite, les données sont filtrées en fonction du type d’échantillon étudié (fécal, cécal ou iléal), ce qui permet d’effectuer des analyses différentes pour chaque compartiment du microbiote intestinal. Pour les échantillons fécaux, le programme génère un graphique représentant l’évolution de la quantité de bactéries vivantes au cours du temps pour chaque souris.
De plus, le programme distingue également les groupes expérimentaux traités par antibiotiques et les groupes placebo grâce à un code couleur, ainsi la comparaison visuelle est facilitée entre les conditions expérimentales. En plus des graphiques, les données traitées sont sauvegardées dans des fichiers CSV différents afin de permettre une analyse plus détaillée.


5. Résultats générés par le programme



En effet, on obtient 3 fichiers dans l'explorateur de fichiers. 
Tout d'abord, un fichier CSV qu'on va analyser: input avec data_small et data_real. Ensuite un fichier image avec les trois graphiques : fecal_plot, cecal_plot et ileal_plot. Enfin, les données sont récupérées sous forme d'un dossier CSV avec quatre fichiers excel : fecal_data, cecal_data, ileal_data et cecal_violin. 


6. Limitations fonctionnelles


   
Ce programme, malgré son bon fonctionnement présente plusieurs limatations: des fonctionnalités implémententées son partiellement fonctionnelles et il y a également des fonctionnalitées non implémentées.


a) Fonctionnalités implémentées mais partiellement ou imparfaitement fonctionnelles



• le programme n'inclut pas encore de gestion avancée des erreurs (par exemple pour les valeurs incorrectes), ainsi que les valeurs aberrantes et manquantes ne sont pas prises en compte.

• La structure des fichiers est supposée être toujours identique et correcte à celle fournie (il n'y a aucune vérification automatique du format qui est effectuée).

• Le programme n'est pas fait pour des fichiers CSV volumineux, en effet, le fichier peut être relu plusieurs fois, ce qui peut ralentir l'exécution pour un grand nombre de données. 

• Le type d'échantillon cécal est identifié par une valeur spécifique ( qui est : ileal_small), ce qui rend le code dépendant du fichier de données fournies.

• Les graphiques génénérés ne sont en effet pas personnalisables par l'utilisaeur, par exemple pour le choix des couleurs, les titres et échelles etc.

• Le programme ne ferme pas explicitement les figures matplotlib après leur sauvegarde, ce qui pourrait poser problème lors d'exécutions répétées du script.


b) Fonctionnalitées non implentées



• Le programme ne permet pas de sélectionner un sous-groupe de souris (par exemple le sexe).

• Le programme ne propose pas d'analyses statistiques complémentaires( par exemple des comparaisons entre groupes, moyennes, tests statistiques, écart-type etc.).


6. Conclusion  



Pour conclure, ce projet permet de manipuler des données expérimentales et de mieux comprendre leur évolution grâce à des graphiques. Même si le programme reste basique et présente certaines limites . Il constitue cependant une bonne base pour analyser des données biologiques. En effet, dans cette étude, nous avons pu analyser l'impact d'un traitement antibiotique sur le microbiote intestinal chez la souris. 






