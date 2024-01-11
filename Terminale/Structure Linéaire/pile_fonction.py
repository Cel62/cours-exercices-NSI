def creer_pile_vide():
    return []

def pile_vide(pile):
    return pile == []

def empiler(element, pile):
    pile.append(element)
    
def depiler(pile):
    pile.pop()
    
def sommet(pile):
    return pile[-1]

def taille(pile):
    return len(pile)