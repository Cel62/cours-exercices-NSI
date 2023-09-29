def creer_grille():
    grille= []
    for i in range(6):
        grille.append([])
        for j in range(7):
            grille[i].append(0)
    return (grille)
            
def afficher_grille(grille):
    for ligne in grille:
        print(end='|')
        for element in ligne:
            if element == 0:
                print(' ', end='|')
            elif element == 1:
                print('X', end='|')
            else:
                print('O', end='|')
        print()

def grille_gagnante(grille):
    for ligne in grille :
        chaine_ligne = ''
        for element in ligne :
            chaine_ligne = chaine_ligne + str(element)
        if '1111' in chaine_ligne or '2222' in chaine_ligne :
            return True
    for colonne in range(7):
        chaine_colonne = ''
        for ligne in range(6):
            chaine_colonne = chaine_colonne + str(grille[ligne][colonne])
        if '1111' in chaine_colonne or '2222' in chaine_colonne:
            return True
    chaine_d1 = ''
    for i in range(4):
        chaine_d1 = chaine_d1 + str(grille[i][3-i])
    if '1111' in chaine_d1 or '2222' in chaine_d1:
        return True
    return False

grille_jeux = creer_grille()

J1 = input('Nom du joueur 1 : ')
J2 = input('Nom du joueur 2 : ')

while True:
    c1 = int(input(J1 + ' - colonne ? '))
    ligne = 5
    while ligne >= 0 and grille_jeux[ligne][c1-1] != 0:
        ligne = ligne - 1
    if ligne >= 0:
        grille_jeux[ligne][c1-1] = 1
    else:
        break
    afficher_grille(grille_jeux)
    if grille_gagnante(grille_jeux):
        print(J1 + " a gagné")
        break
        
    c2 = int(input(J2 + ' - colonne ? '))
    ligne = 5
    while ligne >= 0 and grille_jeux[ligne][c2-1] != 0:
        ligne = ligne - 1
    if ligne >= 0 :
        grille_jeux[ligne][c2-1] = 2
    else :
        break
    afficher_grille(grille_jeux)
    if grille_gagnante(grille_jeux):
        print(J2 + " a gagné")
        break