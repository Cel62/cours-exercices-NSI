import turtle as t

def koch(longueur, n):
    if n == 0:
        t.forward(longueur)
    else:
        koch(longueur/3, n-1)
        t.left(60)
        koch(longueur/3, n-1)
        t.right(120)
        koch(longueur/3, n-1)
        t.left(60)
        koch(longueur/3, n-1)

def flocon(taille, etape):
    koch(taille, etape)
    t.right(120)
    koch(taille, etape)
    t.right(120)
    koch(taille, etape)

flocon(100, 3)