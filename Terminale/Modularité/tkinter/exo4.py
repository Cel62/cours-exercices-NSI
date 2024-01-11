from tkinter import *
from tkinter import messagebox

mafenetre = Tk()
mafenetre.title("Identification requise")
mafenetre.eval('tk::PlaceWindow . center')

motdepasse = StringVar()

def windowMDPCorrect():
    messagebox.showinfo("Résultat", "Mot de passe correct.\nAu revoir !")
    
def windowMDPIncorrect():
    messagebox.showwarning("Résultat", "Mot de passe incorrect.\nVeuillez recommencer.")

def Verification():
    if motdepasse.get() == 'NSI_Branly':
        mafenetre.destroy()
        windowMDPCorrect()
    else:
        mafenetre.destroy()
        windowMDPIncorrect()

text = Label(mafenetre, text = "Mot de passe", fg = 'black')
text.pack(side=LEFT, padx=5, pady=5)

mdpEntry = Entry(mafenetre, textvariable = motdepasse, show = '*')
mdpEntry.pack(side=LEFT, padx=5, pady=5)

BoutonValider = Button(mafenetre, text = 'Valider', command = Verification)
BoutonValider.pack(side=LEFT, padx=5, pady=5)

mafenetre.mainloop()