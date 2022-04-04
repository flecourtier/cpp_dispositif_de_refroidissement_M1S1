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

# Pour lire le fichier "solution_instationnaire_flux_constant.csv"
x=[]
t15=[]
t30=[]
t60=[]
t90=[]
t150=[]
t210=[]
with open('../fichiers_resultats/solution1D_instat_flux_constant.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    count=0
    for row in reader:
        if count==0:
            count+=1
        else:
            x.append(float(row[0]))
            t15.append(float(row[1]))
            t30.append(float(row[2]))
            t60.append(float(row[3]))
            t90.append(float(row[4]))
            t150.append(float(row[5]))
            t210.append(float(row[6]))

# Pour créer le graphique
plt.figure()
plt.plot(x,t15,'r',label="t = 15s")
plt.plot(x,t30,'steelblue',label="t = 30s")
plt.plot(x,t60,'k',label="t = 60s")
plt.plot(x,t90,'gold',label="t = 90s")
plt.plot(x,t150,'darkorange',label="t = 150s",alpha=0.7)
plt.plot(x,t210,'cyan',linestyle='--',label="t = 210s",dashes=(4, 4))
plt.title('Flux de chaleur constant')
plt.xlabel("x (m)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.savefig('../visualisation_graphiques/solution1D_instat_flux_constant.png')

# Pour lire le fichier "solution_instationnaire_activ_desactiv.csv"
t=[]
x0=[]
x1=[]
x2=[]
with open('../fichiers_resultats/solution1D_instat_activ_desactiv.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    count=0
    for row in reader:
        if count==0:
            count+=1
        else:
            t.append(float(row[0]))
            x0.append(float(row[1]))
            x1.append(float(row[2]))
            x2.append(float(row[3]))

# Pour créer le graphique
plt.figure()
plt.plot(t,x0,'steelblue',label="$x_0$")
plt.plot(t,x1,'red',label="$x_{M/2}$")
plt.plot(t,x2,'saddlebrown',label="$x_M$")
plt.title('Avec activation/désactivation du flux de chaleur')
plt.xlabel("time (s)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.savefig('../visualisation_graphiques/solution1D_instat_activ_desactiv.png')