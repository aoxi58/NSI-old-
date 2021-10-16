#-*-coding: utf-8 -*-
# Adrien CHAMBON
# TD 2 - Exercice 6
from math import*
def hex_vers_dec(n):
    nn=str(n)
    Somme=0
    L=len(nn)
    for i in range(L-1,-1,-1):
        
        if nn[i]=='A':
            val="10"
        elif nn[i]=="B":
            val="11"
        elif nn[i]=="C":
            val="12"
        elif nn[i]=="D":
            val="13"
        elif nn[i]=="E":
            val="14"
        elif nn[i]=="F":
            val="15"
        else:
            val=nn[i]
        Res=int(val)*16**(L-1-i)
        Somme=Somme+Res
        
    return Somme




valeur=(input("entrez une valeur "))
print(hex_vers_dec(valeur))
