import csv
import matplotlib.pyplot as plt
from pprint import pprint

# Pour lire le fichier config
with open('../../simu.cfg', newline='') as cfgfile:
    reader = cfgfile.read()
    reader = reader.replace("\r\n", " ").split(" ")
    config = {}
    for key, val in zip(reader[0::2], reader[1::2]):
        config[key] = val

# Pour lire le fichier "convergence_instat_vers_stat.csv"
t=[]
erreur=[]
with open('../fichiers_resultats/convergence_instat_vers_stat.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    count=0
    for row in reader:
        if count==0:
            count+=1
        else:
            t.append(float(row[0]))
            erreur.append(float(row[1]))

# Pour créer le graphique
plt.figure()
plt.plot(t,erreur,label="différence maximale")
plt.title('Convergence du modèle instationnaire vers le modèle stationnaire \n (différence maximale en valeur absolue en fonction du temps)')
plt.xlabel("t (s)")
plt.legend()
plt.savefig('../visualisation_graphiques/convergence_instat_vers_stat.png')