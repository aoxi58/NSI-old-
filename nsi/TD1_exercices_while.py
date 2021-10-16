#-*-coding: utf-8 -*-
# Adrien CHAMBON
# TD 1 - Exercice 11
f=0.05/1000
pli=0
n=int(input("entrez une epaisseur en m"))
while f<=n:
    f=f*2
    pli=pli+1
print("il faut faire",pli,"plis")