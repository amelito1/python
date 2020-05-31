import os
import random
from pprint import pprint
import json

chemin = os.path.dirname(__file__)
chemin = chemin + "/liste.json"
if(not (os.path.isfile(chemin))):
    with open(chemin,"w") as f:
        json.dump([],f)
       
else:
    with open(chemin,"r") as f:
          liste_de_course = json.load(f)
       
affichage ="""
Choisissez une option:
\t1: Ajouter un élément
\t2: Enlever un élément
\t3: Afficher la liste
\t4: Vider la liste
\t5: Terminer\n"""
demande = True
while demande:
    choix = input( affichage)
    if(choix.isdigit()):
        choix = int(choix)
        if(choix == 5):
            demande = False
        if(choix == 1):
            element_a_ajoute = input("que voulez vous ajouter?: ")
            liste_de_course.append(element_a_ajoute)
            with open(chemin,'w') as f:
                json.dump(liste_de_course,f)
                

        elif (choix == 2):
            element_a_retire = input("que voulez vous retirer?: ")
            if(element_a_retire in liste_de_course ):

                liste_de_course.remove(element_a_retire)
                with open(chemin,'w') as f:
                     json.dump( liste_de_course,f)
            else:
                 print(f"element { element_a_retire} est pas dans la liste")
        elif (choix == 3):
             if(len(liste_de_course) == 0):
                print("la liste est vide")
             else:
                 for i in liste_de_course:
                     print("\t"+i+"\n")
        elif (choix == 4):
            
            liste_de_course.clear()
            with open(chemin,'w') as f:
                 json.dump( liste_de_course,f)