"""
Dylan Diaz 05.07.2023
"""
# Importation des modules
from tkinter import *
import random

# Création de la fonction
def generate():
    # Récupération des valeurs
    longueur = longueurMdp.get()
    longueur = int(longueur)
    use_lettre = lettre.get()
    use_chiffre = chiffre.get()
    use_carspe = carspe.get()

    # création des listes de caractères
    lettreList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "v","w", "x", "y", "z"]

    chiffrelList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    caractereSpList = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", ",", ".", "/", "?", "<", ">", "|", "`", "~"]

    # Ajout des listes séléctionner dans une liste vide qui sera utilisé pour générer le mot de passe
    caracteres = []

    if use_lettre:
        caracteres += lettreList
    if use_chiffre:
        caracteres += chiffrelList
    if use_carspe:
        caracteres += caractereSpList

    # Génération du mot de passe
    if not caracteres:
        print("Vous devez choisir au moins une option")
    else:
        mdp = "".join(random.choice(caracteres) for _ in range(longueur))
    
    # Affichage du mot de passe dans la zone de texte
    mdpOutput.delete(0, END)
    mdpOutput.insert(0, mdp)


# Création de la fenêtre
window = Tk()

# Personnalisation de la fenêtre
window.title("Générateur de mot de passe")
window.geometry("720x720")
window.minsize(480, 360)
window.iconbitmap("logo.ico")
window.config(background='#4065A4')

# Création des variables
lettre = IntVar()
chiffre = IntVar()
carspe = IntVar()

# Création de la fram
frame = Frame(window, bg='#4065A4')

# Ajout texte
Label_title = Label(frame, text="Bienvenue dans le générateur de mot de passe 9000!", font=("Helvetica", 18), bg='#4065A4', fg='white')
Label_title.grid(row=0, sticky=N)

Label_subtitle = Label(frame, text="Veuillez indiquez la longueur de votre mot de passe:", font=("Helvetica", 16), bg='#4065A4', fg='white')
Label_subtitle.grid(row=1, sticky=N, pady=30)

Label_subtitle = Label(frame, text="Veuillez choisir les caractères qui seront utiisé pour le mot de passe", font=("Helvetica", 16), bg='#4065A4', fg='white')
Label_subtitle.grid(row=3, sticky=N, pady=20)

# Création de la zone de texte
longueurMdp = Entry(frame, width=5, font=("Helvetica", 16), bg='#4065A4', fg='white')
longueurMdp.grid(row=2, sticky=N)

mdpOutput = Entry(frame, width=30, font=("Helvetica", 16), bg='#4065A4', fg='white')
mdpOutput.grid(row=8, sticky=N, pady=20)

# Création des cases à cocher
c1 = Checkbutton(frame, text="Lettres", font=("Helvetica", 14), bg='#4065A4', variable=lettre)
c1.grid(row=4, sticky=N, pady=5)

c2 = Checkbutton(frame, text="Chiffres", font=("Helvetica", 14), bg='#4065A4', variable=chiffre)
c2.grid(row=5, sticky=N, pady=5)

c3 = Checkbutton(frame, text="Caractère spéciaux", font=("Helvetica", 14), bg='#4065A4', variable=carspe)
c3.grid(row=6, sticky=N, pady=5)

# Création des boutons
generate = Button(frame, text="Générer", font=("Helvetica", 14), bg='#4065A4', fg='white', command=generate)
generate.grid(row=7, sticky=N, pady=20)

# Ajout des frames dans la fenêtre
frame.pack(side=TOP, pady=30)

#Affichage de la fenêtre
window.mainloop()