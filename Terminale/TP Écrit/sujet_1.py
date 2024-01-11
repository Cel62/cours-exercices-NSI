def creer_pile_vide():
    return []

def est_vide(pile):
    if pile == []:
        return True

def empiler(pile, element):
    pile.append(element)

def depiler(pile):
    return pile.pop()

P = [8, 5, 2, 4]

def hauteur_pile(P):
    Q = creer_pile_vide()
    n = 0
    while not (est_vide(P)):
        n += 1
        x = depiler(P)
        empiler(Q, x)
    while not (est_vide(Q)):
        x = depiler(Q)
        empiler(P, x)
    return n

