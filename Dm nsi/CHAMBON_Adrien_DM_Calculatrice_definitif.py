#-*-coding: utf-8 -*-
# Adrien CHAMBON
# TD 2 - Exercice 6
from math import*

# partie fonction

def addition(a,b):
    res=a+b
    return res
def sousrtaction(a,b):
    res=a-b
    return res
def multiplication(a,b):
    res=a*b 
    return res
def division(a,b):
    res=a/b
    return res

def divisioneucli(a,b):
    res=a//b
    reste=a%b
    return 'quotient : ',res, 'reste : ',reste
def exposant(a,b):
    res=a**b
    return res
# programme principal

sortir=False
while sortir==False :
    print("# quelle operation voulez vous effectuer ?")
    print("# addition : tapez 1")
    print("# soustraction : tapez 2")
    print("# multiplication : tapez 3")
    print("# division : tapez 4")
    print("# division euclidienne : tapez 5")
    print("# exposant : tapez 6")


    choix=int(input("# votre choix : "))
    a=int(input("# entrez la premiere operande : "))
    b=int(input("# entrez la seconde operande : "))
    if choix==1 :
        print("#",addition(a,b))
    elif choix==2 :
        print("#",sousrtaction(a,b))
    elif choix==3 :
        print("#",multiplication(a,b))
    elif choix==4 :
        print("#",division(a,b))
    elif choix==5 :
        print("#",divisioneucli(a,b))
    elif choix==6 :
        print("#",exposant(a,b))
    fin=input("# voulez vous continuer ? tapez oui ou non : ")
    if fin=="non":
        sortir=True

