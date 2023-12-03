# Initialisation du jeu

# 1 - Importez les bibliothèques nécessaires : Tkinter et tkinter.messagebox.
# Pour importer les bibliothèques nécessaires, il faut procéder ainsi
import tkinter as tk
from tkinter import messagebox

# 2 - Créez une fenêtre Tkinter avec le titre "TIC-TAC-TOE".
# Pour créer une fenêtre Tkinter avec le titre "TIC-TAC-TOE"
fenetre = tk.Tk()
fenetre.title("TIC-TAC-TOE")

# 3 - Définissez une liste appelée chiffres avec les chiffres de 1 à 9 pour représenter les positions disponibles sur le plateau de jeu.
# Définissez une liste appelée chiffres avec les chiffres de 1 à 9 pour représenter les positions disponibles sur le plateau de jeu
chiffres = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 4 - Initialisez la variable mark à une chaîne vide ('').
# Initialisez la variable mark à une chaîne vide ('')
mark = ''

# 5 - Définissez la variable count sur 0 pour suivre le nombre de mouvements.
# Définissez la variable count sur 0 pour suivre le nombre de mouvements
count = 0

# 6 - Créez une liste appelée panneaux avec 10 éléments, où le premier élément est un espace réservé (« panneau »)
# et le reste représente les positions du plateau de jeu.
# Créez une liste appelée panneaux avec 10 éléments, où le premier élément est un espace réservé et le reste représente les positions du plateau de jeu
panneaux = [' '] * 10


# PHASE DE PRESENTATION

# 1 - Définissez la fonction de vérificateur avec un seul paramètre, chiffre.
# Définissez la fonction de vérificateur
def verifier(chiffre):

# 2 - À l'intérieur de la fonction, déclarez les variables count, mark et digits comme variables globales.
    # Déclarez les variables count, mark et digits comme variables globales
    global count, mark, chiffres

# 3 - Écrivez une série d'instructions if pour gérer différentes valeurs numériques de 1 à 9.
# Série d'instructions if pour gérer différentes valeurs numériques de 1 à 9
    if chiffre == 1 and 1 in chiffres:
        chiffres.remove(1)
        update_board(1)


    elif chiffre == 2 and 2 in chiffres:
        chiffres.remove(2)
        update_board(2)

    elif chiffre == 3 and 3 in chiffres:
        chiffres.remove(3)
        update_board(3)

    elif chiffre == 4 and 4 in chiffres:
        chiffres.remove(4)
        update_board(4)

    elif chiffre == 5 and 5 in chiffres:
        chiffres.remove(5)
        update_board(5)

    elif chiffre == 6 and 6 in chiffres:
        chiffres.remove(6)
        update_board(6)

    elif chiffre == 7 and 7 in chiffres:
        chiffres.remove(7)
        update_board(7)

    elif chiffre == 8 and 8 in chiffres:
        chiffres.remove(8)
        update_board(8)

    elif chiffre == 9 and 9 in chiffres:
        chiffres.remove(9)
        update_board(9) # Fonction pour mettre à jour le plateau de jeu
# 4 - Pour chaque instruction if, vérifiez si le chiffre saisi correspond à la condition
# et existe dans la liste des chiffres.


# 5 - Si la condition est satisfaite, supprimez le chiffre de la liste des chiffres et procédez à la mise à jour du plateau
# de jeu en fonction du tour du joueur actuel.
# Fonction pour mettre à jour le plateau de jeu
def update_board(chiffre):
    global count, mark

# 6 - Déterminez la marque du joueur actuel (« X » ou « O ») en fonction de la variable de comptage (pair ou impair).
    # Déterminez la marque du joueur actuel (« X » ou « O ») en fonction de la variable de comptage (pair ou impair)
    mark = 'X' if count % 2 == 0 else 'O'

# 7 - Mettez à jour le bouton correspondant sur le plateau de jeu (bouton 1 pour le chiffre 1, bouton 2 pour le chiffre 2, etc.)
# avec la marque actuelle.
# Mettez à jour le bouton correspondant sur le plateau de jeu avec la marque actuelle
    buttons[chiffre-1].config(text=mark, state=tk.DISABLED)

# 8 - Incrémentez la variable count pour garder une trace du nombre de mouvements effectués.
    # Incrémentez la variable count pour garder une trace du nombre de mouvements effectués
    count += 1

# 9 - Vérifiez si le joueur actuel a gagné la partie en appelant la fonction win
# et en comparant le résultat avec la marque actuelle (« X » ou « O »).

# 10 - Si le joueur actuel a gagné, affichez un message d'information indiquant le gagnant ("Joueur1 gagne" ou "Joueur2 gagne")
# et détruisez la fenêtre de jeu (root.destroy()).

# 11 - Répétez les étapes 3 à 10 pour chaque chiffre de 2 à 9.

# 12 - Après la dernière instruction if, vérifiez si le jeu a abouti à une égalité en vérifiant si la variable count est supérieure à 8
# (indiquant que tous les mouvements ont été effectués) et qu'aucun joueur n'a gagné.

# 13 - En cas d'égalité, affichez un message d'information indiquant "Match nul" et détruisez la fenêtre de jeu.

  # Vérifiez si le joueur actuel a gagné
    if win():
        messagebox.showinfo("Tic-Tac-Toe", f"Joueur {mark} gagne!")
        fenetre.destroy()   # Détruisez la fenêtre de jeu

    # Vérifiez si le jeu a abouti à une égalité
    elif count > 8 and not win():
        messagebox.showinfo("Tic-Tac-Toe", "Match nul!")
        fenetre.destroy()  # Détruisez la fenêtre de jeu
