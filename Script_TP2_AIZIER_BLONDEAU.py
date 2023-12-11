#Hugo AIZIER et Antoine BLONDEAU

import csv
import matplotlib.pyplot as plt
import numpy as np





###fonction###
def energie(date,heure):
    renou = 0
    fos = 0
    for liste in table :
        if liste[2] == date and liste[3] == heure :
            fos += int(liste[7]) + int(liste[8]) + int(liste[9]) +int(liste[10])
            renou += int(liste[11])+ int(liste[12]) + int(liste[13]) + int(liste[14]) + int(liste[15])  #7,8,9,10 = fossile et 11 à 15 = renouvlable
    return renou,fos




'''heure avec le plus de conso dans 2020'''



table=[]
with open('RTE_2020.csv',newline='') as csvfile:            #ouverture du fichier et stockage dans une liste nommée table.
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        table.append(row)

del table[0]                                                #on supprimé la première ligne du fichier


liste_conso_heure=[]                                        #permet de récupérer et de stocker dans un dico les heures et la consomation associé.
for elt in table:
    if elt[4]!='':
        liste_conso_heure.append([elt[2],elt[3],elt[4]])



max=[0,0,0]                                                 #max contient désormais la date,l'heure et la conso du jour dans l'année 2020 où on a le plus consommé
for date,heure,conso in liste_conso_heure:
    a=int(conso)
    if a > int(max[2]):
        max=[date,heure,conso]


renou = 0
non_renou = 0
L=[0,0]
for liste in table :
    if liste[2] == max[0] and liste[3] == max[1] :
        non_renou += int(liste[7]) + int(liste[8]) + int(liste[9]) +int(liste[10])
        renou += int(liste[11])+ int(liste[12]) + int(liste[13]) + int(liste[14]) + int(liste[15]) + int(liste[16])
        L = [non_renou,renou]



energies = ['non renouvelable','renouvelable']
plt.pie(L, labels=energies,autopct='%1.1f%%',startangle=30)
plt.title("Heure avec le plus de conso dans l'année 2020")
plt.legend()
plt.show()



'''graph évolution année 2020'''  #non fonctionnel
'''
gh=True
liste_nr=[]
liste_r=[]
while gh==True:
    for truc in table:
        if truc[4]!='':
            ren=0
            n_ren=0
            for i in range(48):
                n_ren += int(truc[7]) + int(truc[8]) + int(truc[9]) +int(truc[10])
                ren += int(truc[11])+ int(truc[12]) + int(truc[13]) + int(truc[14]) + int(truc[15]) + int(truc[16])
        liste_nr.append(n_ren)
        liste_r.append(ren)
    gh=False
print(len(liste_nr))
print(len(liste_r))
liste_journee=[]
for i in range(1,366):
    liste_journee.append(i)
print(len(liste_journee))
plt.plot(liste_r,liste_journee,color='r')
plt.plot(liste_nr,liste_journee,color='b')
plt.title('graph')
plt.show()


'''


"""Consommation de toute l'année"""
e_r = 0                                                     #énergies renouvelable
e_n = 0                                                     #énergies non renouvelable
for e in table :                                            
    if e[4] !='':
        e_n += int(e[7]) + int(e[8]) + int(e[9]) +int(e[10])
        e_r += int(e[11])+ int(e[12]) + int(e[13]) + int(e[14]) + int(e[15]) + int(e[16])
L_totale = [e_n,e_r]


plt.pie(L_totale, labels=energies,autopct='%1.1f%%',startangle=24)
plt.title("Consommation de toute l'année")
plt.legend()
plt.show()


