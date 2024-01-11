def somme(l):
    if len(l) == 0:
        return 0
    return somme(l[1:]) + l[0]

def u(n):
    if n == 0:
        return 5
    return 2 * u(n - 1) + 7