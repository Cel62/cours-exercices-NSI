from tkinter import *

mafenetre = Tk()
mafenetre.title("Affichage images")
mafenetre.geometry("600x600")
    
Canevas = Canvas(mafenetre, width=500, height=500, background='white')

photo = PhotoImage(file='java-logo.gif')
item1 = Canevas.create_image(200, 0, anchor='n', image=photo)
Canevas.pack()

BoutonQuitter = Button(mafenetre, text = 'Quitter', command = mafenetre.destroy)
BoutonQuitter.pack(side=LEFT, padx=5, pady=5)

mafenetre.mainloop()  