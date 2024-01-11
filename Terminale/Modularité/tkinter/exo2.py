from tkinter import *

# Création de la fenêtre principale
Mafenetre=Tk()

# Création d'un widget Label
Label1 = Label(Mafenetre, text = 'Bienvenue au lycée Branly', fg = 'red')
Label1.pack()

# Création d'un widget Button
Bouton1 = Button(Mafenetre, text = 'Quitter', command = Mafenetre.destroy)
Bouton1.pack()

# Lancement de la boucle infinie (gestionnaire d'événements)
Mafenetre.mainloop()