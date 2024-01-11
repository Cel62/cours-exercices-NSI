def fonct(n):
    if n > 0:
        fonct(n-1)
    print(n)

fonct(3)

def eq_fonct(n):
    for i in range(n + 1):
        print(i)