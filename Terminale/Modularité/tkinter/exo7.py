from tkinter import *

mafenetre = Tk()
mafenetre.title("Carrés")
mafenetre.geometry("500x360")

Canevas = Canvas(mafenetre, width=480, height=320, background='white')
Canevas.focus_set()
pion = Canevas.create_oval(10, 10, 20, 20, width=2, outline="black", fill="red")

posX = 10
posY = 10

def Clavier(event):
    global posX
    global posY
    
    touche = event.keysym
    
    if touche == "h":
        posY -= 1
    if touche == 'b':
        posY += 1
    if touche == 'g':
        posX -= 1
    if touche == 'd':
        posX += 1
        
    Canevas.coords(pion, posX, posY, posX + 10, posY + 10)

def Clic(event):
    Canevas.create_rectangle(event.x, event.y, event.x + 40, event.y + 40, outline='black', fill='blue')

Canevas.bind("<KeyPress>", Clavier)
Canevas.bind("<B1-Motion>", Clic)
Canevas.pack()

BoutonQuitter = Button(mafenetre, text = 'Quitter', command = mafenetre.destroy)
BoutonQuitter.pack(side=LEFT, padx=5, pady=5)

mafenetre.mainloop()