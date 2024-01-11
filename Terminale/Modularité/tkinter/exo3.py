from tkinter import *
import random

mafenetre = Tk()
mafenetre.title("Jeu de dé")
mafenetre.eval('tk::PlaceWindow . center')

newText = StringVar(mafenetre, "Résultat -> ")

def NouveauLance():
    nb = random.randint(1, 6)
    newText.set("Résultat -> " + str(nb))

BoutonLancer = Button(mafenetre, text = 'Lancer', command = NouveauLance)
BoutonLancer.pack(side=LEFT, padx=5, pady=5)

BoutonQuitter = Button(mafenetre, text = 'Quitter', command = mafenetre.destroy)
BoutonQuitter.pack(side=LEFT, padx=5, pady=5)

text = Label(mafenetre, textvariable = newText, fg = 'blue', bg = 'white')
text.pack(side=LEFT, padx=5, pady=5)

mafenetre.mainloop()