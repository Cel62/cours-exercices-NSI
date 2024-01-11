import numpy as np
import matplotlib.pyplot as plt

def trace(a, b, f, n):
    Lx = np.linspace(a, b, n)
    Ly = [f(x) for x in Lx]
    plt.plot(Lx, Ly)
    plt.show()
    
def g(x):
    return x**2 + 2*x + 1

# trace(-1, 5, g, 50)