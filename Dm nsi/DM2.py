import math
import random

jeu = ['pierre', 'feuille', 'ciseaux', 'lesard', "spock"]


def menu():
    MenuChoix=int(input("""# Bienvenue, pour jouer au Jeu Pierre, Feuille, Ciseaux, lézard, Spock,
# tapez 1 pour le mode facile, tapez 2 pour le mode difficile : """))
    if MenuChoix==1:
        facile()
    elif MenuChoix==2:
        difficile()


# mode facile 
def facile():

    bot = random.choice(jeu)

    choix = input('# Choisissez entre "pierre", "feuille", "ciseaux" "lesard" ou "spock" !   :  ')
    # on traite le cas d'une égalité
    if(choix == bot):
        print('Egalité ! Le robot a choisit', bot, 'comme vous !')
    else:
        # on traite le cas d'une victoire
        if(choix == 'pierre' and (bot == 'ciseaux' or bot =="lesard")):
            print("# Vous avez gagné ! L'IA a choisi", bot, "!")

        elif(choix == "feuille" and (bot == "pierre" or bot == "spock")):
            print("# Vous avez gagné ! L'IA a choisi", bot, "!")

        elif(choix == "ciseaux" and (bot == "feuille" or bot == "lesard")):
            print("# Vous avez gagné ! L'IA a choisi", bot, "!")

        elif(choix == "lesard" and (bot == "spock" or bot == "feuille")):
            print("# Vous avez gagné ! L'IA a choisi", bot, "!")
        
        elif(choix == "spock" and (bot == "ciseaux" or bot == "pierre")):
            print("# Vous avez gagné ! L'IA a choisi", bot, "!")
       
       # on traite le cas d'une défaite
        elif(choix == "lesard" and (bot == "pierre" or bot == "ciseaux")):
            print("# Vous avez perdu ! L'IA a choisi", bot, "!")

        elif(choix == "spock" and (bot == "feuille" or bot == "lesard")):
            print("# Vous avez perdu ! L'IA a choisi", bot, "!")

        elif(choix == "pierre" and (bot == "feuille" or bot == "spock")):
            print("# Vous avez perdu ! L'IA a choisi", bot, "!")

        elif(choix == "feuille" and (bot == "ciseaux" or bot == "lesard")):
            print("# Vous avez perdu ! L'IA a choisi", bot, "!")

        elif(choix == "ciseaux" and (bot == "spock" or bot == "pierre")):
            print("# Vous avez perdu ! L'IA a choisi", bot, "!")   
        
        # on traite le cas d'une erreur
        else:
            print('# Une erreur est survenue !')

    rejouer()

# mode difficile
def difficile():
    PlayerWin=0
    IaWin=0

    for i in range(3):
        bot = random.choice(jeu)
        choix = input('# Choisissez entre "pierre", "feuille", "ciseaux" "lesard" ou "spock" !   :  ')
        # on traite le cas d'une égalité
        if(choix == bot):
            print('# Egalité ! Le robot a choisit', bot, 'comme vous !')
        else:
        # on traite le cas d'une victoire
            if(choix == 'pierre' and (bot == 'ciseaux' or bot =="lesard")):
                print("# Vous avez gagné ! L'IA a choisi", bot, "!")
                PlayerWin=PlayerWin+1

            elif(choix == "feuille" and (bot == "pierre" or bot == "spock")):
                print("# Vous avez gagné ! L'IA a choisi", bot, "!")
                PlayerWin=PlayerWin+1

            elif(choix == "ciseaux" and (bot == "feuille" or bot == "lesard")):
                print("# Vous avez gagné ! L'IA a choisi", bot, "!")
                PlayerWin=PlayerWin+1

            elif(choix == "lesard" and (bot == "spock" or bot == "feuille")):
                print("# Vous avez gagné ! L'IA a choisi", bot, "!")
                PlayerWin=PlayerWin+1
        
            elif(choix == "spock" and (bot == "ciseaux" or bot == "pierre")):
                print("# Vous avez gagné ! L'IA a choisi", bot, "!")
                PlayerWin=PlayerWin+1
       
       # on traite le cas d'une défaite
            elif(choix == "lesard" and (bot == "pierre" or bot == "ciseaux")):
                print("# Vous avez perdu ! L'IA a choisi", bot, "!")
                IaWin=IaWin+1

            elif(choix == "spock" and (bot == "feuille" or bot == "lesard")):
                print("# Vous avez perdu ! L'IA a choisi", bot, "!")
                IaWin=IaWin+1

            elif(choix == "pierre" and (bot == "feuille" or bot == "spock")):
                print("# Vous avez perdu ! L'IA a choisi", bot, "!")
                IaWin=IaWin+1

            elif(choix == "feuille" and (bot == "ciseaux" or bot == "lesard")):
                print("# Vous avez perdu ! L'IA a choisi", bot, "!")
                IaWin=IaWin+1

            elif(choix == "ciseaux" and (bot == "spock" or bot == "pierre")):
                print("# Vous avez perdu ! L'IA a choisi", bot, "!")
                IaWin=IaWin+1   
        
        # on traite le cas d'une erreur
            else:
                print('# Une erreur est survenue !')

    if PlayerWin<IaWin:
        print("# L'IA a remportée la partie")
    elif PlayerWin==IaWin:
        print("# Il y a égalité")
    elif PlayerWin>IaWin:
        print("# Vous avez gagné la partie !")
    rejouer()


    

def rejouer():
    choix2 = input('# Voulez vous rejouer ? (Y/N)   :   ')
    if(choix2 == 'Y'):
        menu()
    if(choix2 == 'y'):
        menu()
    if(choix2 == 'yes'):
        menu()
    else:
        exit

menu()