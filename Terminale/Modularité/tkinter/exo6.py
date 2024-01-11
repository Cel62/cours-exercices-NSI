from tkinter import *

mafenetre = Tk()
mafenetre.title("Carrés")
mafenetre.geometry("500x360")

Canevas = Canvas(mafenetre, width=480, height=320, background='white')

def Clic(event):
    Canevas.create_rectangle(event.x, event.y, event.x + 40, event.y + 40, outline='black', fill='blue')

def Effacer():
    Canevas.delete('all')

Canevas.bind("<B1-Motion>", Clic)
Canevas.pack()

BoutonQuitter = Button(mafenetre, text = 'Effacer', command = Effacer)
BoutonQuitter.pack(side=LEFT, padx=5, pady=5)

BoutonQuitter = Button(mafenetre, text = 'Quitter', command = mafenetre.destroy)
BoutonQuitter.pack(side=LEFT, padx=5, pady=5)

mafenetre.mainloop()