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
    # pprint(config)

# Pour lire le fichier "solution_stationnaire_Lx{Lx}.csv"
x=[]
sol=[]
sol_exacte=[]
with open('../fichiers_resultats/solution1D_stat_Lx'+config['Lx']+'.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    count=0
    for row in reader:
        if count==0:
            count+=1
        else:
            x.append(float(row[0]))
            sol.append(float(row[1]))
            sol_exacte.append(float(row[2]))

# Pour créer le graphique
plt.figure()
plt.plot(x,sol,"steelblue",label="numeric",alpha=0.7)
plt.plot(x,sol_exacte,"--r",label="exact",dashes=(4, 4))
plt.title("Lx="+config['Lx'])
plt.xlabel("x (m)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.savefig('../visualisation_graphiques/solution1D_stat_Lx'+config['Lx']+'.png')