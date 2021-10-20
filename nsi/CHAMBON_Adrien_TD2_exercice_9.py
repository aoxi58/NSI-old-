#-*-coding: utf-8 -*-
# Adrien CHAMBON
# TD 2 - Exercice 6
from math import*
def dec_vers_hex(n):
    somme=""
    while n!=0:
        reste=n%16
        if reste==10:
            reste="A"
        elif reste==11:
            reste="B"
        elif reste==12:
            reste="C"
        elif reste==13:
            reste="D"
        elif reste==14:
            reste="E"
        elif reste==15:
            reste="F"
        n=n//16
        somme=str(reste)+somme
    return somme
valeur=int(input("entrez une valeur"))
print(dec_vers_hex(valeur))