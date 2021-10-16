#-*-coding: utf-8 -*-
# Adrien CHAMBON
# TD 1 - Exercice 9
from random import*
inconnue=randint(0,1000)
for i in range (10):
    n=int(input("entrez un nombre"))
    if inconnue>n:
        print("c'est plus")
    elif inconnue<n:
        print("c'est moins")
    elif inconnue==n:
        print("c'est gagné")
if inconnue!=n        
    print("c'est perdu")