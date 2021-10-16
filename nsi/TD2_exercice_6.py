#-*-coding: utf-8 -*-
# Adrien CHAMBON
# TD 2 - Exercice 6
from math import*

def bin_vers_dec(n):
    nn=str(n)
    Somme=0
    L=len(nn)
    for i in range(L-1,-1,-1):
        Res=int(nn[i])*2**(L-1-i)
        Somme=Somme+Res
    return Somme





valeur=int(input("entrez une valeur"))
print(bin_vers_dec(valeur))
