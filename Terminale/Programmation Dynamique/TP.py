tab = [[5], [8, 10], [11, 3, 4], [6, 10, 7, 12]]

def solution_naive(t, l, r):
    if l == len(t) - 1:
        return t[l][r]
    
    return t[l][r] + max(solution_naive(t, l + 1, r), solution_naive(t, l + 1, r + 1))

def solution_dynamique():
    m = []
    for x in range(len(tab)):
        t = []
        for _ in range(len(tab[x])):
            t.append(0)
        m.append(t)
    return solution_dynamique_mem(0, 0, m)

def solution_dynamique_mem(l, c, m):
    if l == len(tab) - 1:
        return tab[l][c]
    elif m[l][c] != 0:
        return m[l][c]
    v =  max(solution_dynamique_mem(l + 1, c, m), solution_dynamique_mem(l + 1, c + 1, m)) + tab[l][c]
    m[l][c] = v
    return v