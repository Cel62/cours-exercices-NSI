def fib_mem(n):
    mem = [0] * (n+1)
    return fib_mem_c(n, mem)

def fib_mem_c(n, m):
    if n == 0 or n == 1:
        m[n] = n
        return n
    elif m[n] > 0:
        return m[n]
    else:
        m[n] = fib_mem_c(n-1, m) + fib_mem_c(n-2, m)
        return m[n]

pieces = (2, 5, 10, 50, 100)
def rendu_monnaie_mem(P,X):
    mem = [0]*(X+1)
    return rendu_monnaie_mem_c(P,X,mem)

def rendu_monnaie_mem_c(P,X,m):
    if X==0:
        return 0
    elif m[X]>0:
        return m[X]
    else:
        mini = 1000
        for i in range(len(P)):
            if P[i]<=X:
                nb = 1+rendu_monnaie_mem_c(P,X-P[i],m)
                if nb<mini:
                    mini = nb
                    m[X] = mini
    return mini

pieces = (2,5,10,50,100)