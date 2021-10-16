#-*-coding: utf-8 -*-
# Adrien CHAMBON
# TD 2 - Exercice 6
from math import*
def dec_vers_bin(n):
    somme=""
    while n!=0:
        reste= n%2
        n=n//2
        somme=str(reste)+somme
    return somme
valeur=int(input("entrez une valeur"))
print(dec_vers_bin(valeur))