import turtle

turtle.setup(507, 380)  #Largeur : 507px, Hauteur : 380px, position centrée -> Pour avoir une zone dessin identique à l'oeuvre

def position_en(x, y, orientation = 0):
    """ fonction (en fait une procédure) qui place la tortue en un point x,y repéré par rapport au coin supérieur gauche
    et l'oriente selon la valeur de orientation
    :param x,y:  (int) les coordonnées où placer la tortue
    :param orientation: (int) 0 = Est ; 90 = Nord; 180 = Ouest ; 270 = Sud ;
    """
    turtle.penup()
    turtle.setposition(x - turtle.window_width()//2, turtle.window_height()//2 - y)
    turtle.setheading(orientation)
    turtle.pendown()
    
def ligne_h(y, epaisseur = 10, trait='black'):
    """ procédure pour tracer une ligne horizontale
    :param y: (int) l'ordonnée de la ligne (par rapport au coin supérieur gauche)
    :param epaisseur: (int) l'épaisseur du trait en pixel
    :param trait: (str) la couleur du trait
    """
    pass
    
def ligne_v(x, epaisseur = 10, trait='black'):
    """ procédure pour tracer une ligne horizontale
    :param x: (int) l'abscisse de la ligne (par rapport au coin supérieur gauche)
    :param epaisseur: (int) l'épaisseur du trait en pixel
    :param trait: (str) la couleur du trait
    """
    pass
    
def rectangle(x1, y1, x2, y2, couleur = "red", epaisseur = 10, trait = 'black'):
    """ procédure pour tracer un rectangle coloré entouré d'un trait
    :param x1, y1: (int) les coordonnées du coin supérieur gauche du rectangle
    :param x2, y2: (int) les coordonnées du coin inférieur droit du rectangle
    :param couleur (string) couleur de remplissage du rectangle (rouge par défaut)
    :param epaisseur: (int) l'épaisseur du trait en pixel (10 px par défaut)
    :param trait: (str) la couleur du trait (noir par défaut)
    """
    pass       
        
# dessinons
# 3 traits horizontaux
pass
# 4 traits verticaux
pass
# 1 rectangle rouge
pass
# 1 rectangle bleu
pass
# 1 rectangle jaune
pass

# enregistrons le travail
turtle.getscreen()
turtle.getcanvas().postscript(file="modrian.eps")