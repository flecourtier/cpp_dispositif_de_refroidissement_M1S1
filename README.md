# cpp_dispositif_de_refroidissement_M1S1
Projet de C++ guidé en M1S1 : dispositif de refroidissement d'un microprocesseur

Sujet proposé par Vincent Chabannes (voir "sujet_projet.pdf")

Ce projet a pour but de réaliser un programme C++ permettant d'étudier le comportement thermique d'un dispositif de refroidissement d'un micro-processeur. Nous allons nous intéresser uniquememt à la simulation thermique d'une seule ailette du dissipateur.

**Pour plus de détail sur le projet et sur son utilisation, consulter le fichier rapport.pdf.**

## Comment compiler et exécuter le projet ?

Un fichier "CMakeLists.txt" a été créé, il suffit de créer un repertoire (build par exemple) puis de faire cmake et make pour compiler le programme.

Un fichier nommé "simu.cfg" a été créé afin de pouvoir modifier les paramètres du modèle. Dans celui-ci une variale stationnary permet de choisir le cas que l'on souhaite (0 pour un modèle instationnaire et 1 pour un modèle stationnaire).

Une fois les paramètres choisis, il suffit d'exécuter run.e qui va nous créer les fichiers ".csv" et ".vtk" voulus.

## Comment obtenir les résultats visuels ?

Pour une question de simplicité, j’ai décidé de créer un script shell nommé "graphique.sh" qui permet de générer les graphiques et vidéos à partir des fichiers ".csv" et ".vtk" qui se trouvent dans le répertoire fichiers_resultats (après l’exécution du programme). Ce script utilise des fichiers python qui créent les images et graphiques souhaités. 

Les fichiers python qui permettent la création des représentations en 3D ont été générés grâce à l’outil Trace proposé par Paraview. Cet outil permet d’exporter l’ensemble des actions effectuées sur le logiciel sous la forme d’un script python. Il a tout de même fallu effectuer quelques modifications de ces scripts.
A noter que l’installation d’un programme nommé pvpython m’a été nécessaire pour exécuter ces scripts. De plus, pour les graphiques en 1D, seul matplotlib a été nécessaire.

Ainsi, pour éviter de devoir manipuler ces fichiers python, un script shell nommé "graphique.sh" a été créé. Pour l’exécuter il suffit de se trouver dans le répertoire resultats. Ce script prend en paramètre un argument permettant de choisir quelles image et/ou vidéos seront créées. L’exécution de ce script sans argument (via la
commande "./graphique.sh") affiche une aide indiquant les choix possibles pour le paramètre. 

Si tous les fichiers du modèle instationnaire et du modèle stationnaire ont été créés (c'est-à-dire on a executé le code avec stationnary=0 et stationnary=1), l'exécution du scrpit "graphique.sh" avec l'argument 0 permettra de créer tous les graphiques (images et vidéos). A noter que la création des vidéos peut être un peu longue.
