from tkinter import *
import random
import time

points_score = 0
game_start = False

class Balle:
    def __init__(self, canvas, raquette, couleur):
        self.canvas = canvas
        self.raquette = raquette
        self.id = canvas.create_oval(10, 10, 25, 25, fill=couleur)
        self.canvas.move(self.id, 245, 100)
        
        departs = [-3, -2, -1, 1, 2, 3]
        random.shuffle(departs)
        self.x = departs[0]
        self.y = -3
        
        self.largeur_canevas = self.canvas.winfo_width()
        self.hauteur_canevas = self.canvas.winfo_height()
        
        self.touche_bas = False
        
    def heurter_raquette(self, pos):
        pos_raquette = self.canvas.coords(self.raquette.id)
        if pos[2] >= pos_raquette[0] and pos[0] <= pos_raquette[2]:
            if pos[3] >= pos_raquette[1] and pos[3] <= pos_raquette[3]:
                return True
        return False
    
    def dessiner(self):
        global points_score
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.hauteur_canevas:
            self.touche_bas = True
        if self.heurter_raquette(pos) == True:
            self.y = -6
            points_score += 1
            points_text.set("Score : " + str(points_score))
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.largeur_canevas:
            self.x = -3

class Raquette:
    def __init__(self, canvas, couleur):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=couleur)
        self.canvas.move(self.id, 200, 300)
        
        self.x = 0
        
        self.largeur_canvas = self.canvas.winfo_width()
        
        self.canvas.bind_all("<KeyPress-Left>", self.vers_gauche)
        self.canvas.bind_all("<KeyPress-Right>", self.vers_droite)

    def dessiner(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.largeur_canvas:
            self.x = 0
    
    def vers_gauche(self, event):
        global game_start
        if game_start == False:
            game_start = True
        self.x = -4
        
    def vers_droite(self, event):
        global game_start
        if game_start == False:
            game_start = True
        self.x = 4

tk = Tk()
tk.title("Jeu")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()

points_text = StringVar(tk, "Score : 0")

score = Label(tk, textvariable=points_text)
score.pack()

partieTermine = canvas.create_text(250, 200, text="Partie terminée", state="hidden")

tk.update()

raquette = Raquette(canvas, "blue")
balle = Balle(canvas, raquette, "red")

while 1:
    if balle.touche_bas == False:
        if game_start == True:
            balle.dessiner()
        raquette.dessiner()
    else:
        canvas.itemconfig(partieTermine, state="normal")
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)