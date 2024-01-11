def nb_chiffres(n):
    if n == 0:
        return 0
    return 1 + nb_chiffres(n // 10)

def syracuse(u_n):
    if u_n <= 1:
        return "Fin"
    print(u_n)
    if u_n % 2 == 0:
        return syracuse(u_n / 2)
    return syracuse(3 * u_n + 1)
    
def pgcd(a, b):
    if b == 0:
        return a
    return pgcd(b, a % b)

def est_palindrome(mot):
    if len(mot) < 2:
        return True
    if mot[0] == mot[-1]:
        return est_palindrome(mot[1:-1])
    return False

def somme_element(liste_elements):
    if len(liste_elements) == 0:
        return 0
    return somme_element(liste_elements[1:]) + liste_elements[0]

def hanoi(n, a = 1, b = 2, c = 3):
    if n > 0:
        hanoi(n - 1, a, c, b)
        print ("Disque de taille ", n, " déplacé de la tour ", a, " à la tour ", c)
        hanoi(n - 1, b, a, c)