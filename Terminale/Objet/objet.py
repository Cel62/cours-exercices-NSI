import random

class Personnage:
    def __init__(self, nbreDeVie):
        self.vie = nbreDeVie
    
    def donneEtat (self):
        return self.vie
    
    def perdVie (self):
        if random.random() > 0.5:
            nbPoint = 1
        else:
            nbPoint = 2
        self.vie -= nbPoint
    
    def boirePotion(self):
        if random.random() > 0.5:
            nbPoint = 1
        else:
            nbPoint = 2
        self.vie += nbPoint
    
def game():
    bilbo = Personnage(20)
    gollum = Personnage(20)
    while bilbo.donneEtat() > 0 and gollum.donneEtat() > 0 :
        bilbo.perdVie()
        gollum.perdVie()
        bilbo.boirePotion()
        gollum.boirePotion()
    if bilbo.donneEtat() <= 0 and gollum.donneEtat() > 0:
        msg = f"Gollum est vainqueur, il lui reste encore {gollum.donneEtat()} points alors que Bilbo est mort"
    elif gollum.donneEtat() <= 0 and bilbo.donneEtat() > 0:
        msg = f"Bilbo est vainqueur, il lui reste encore {bilbo.donneEtat()} points alors que Gollum est mort"
    else :
        msg = "Les deux combattants sont morts en même temps"
    return msg