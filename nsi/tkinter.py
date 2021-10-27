from tkinter import*
#On crée la fenêtre
fenetre = Tk()
#On crée un label ( texte à afficher ) qui a pour contenant la fenetre
texte = Label ( fenetre , text ="Hello world")
#On détermine la position géométrique du texte dans le contenant
#Ici , le contenant aura une taille adaptée au texte ( méthode pack )
texte . pack ()
fenetre . mainloop ()