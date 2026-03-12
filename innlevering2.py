import numpy as np
import matplotlib.pyplot as plt

# Funksjonen f(x) og f´(x)
def f(x):
    return np.exp(-x/4) * np.arctan(x)

def f_d(x):
    return -np.exp(-x/4)/4 * (np.arctan(x) - (4 / (1 + x**2)))

def halveringsmetode(a, b, n):
    """ Halveringsmetoden (midtpunktmetoden) for løsning av likning på formen f(x)=0. 
    Startverdier a og b velges hvor f(a) og f(b) har motsatt fortegn.
    Antall desimaler n som ønskes med sikkerhet i svaret """
    
    f_a = f_d(a) 

    pres = 1/10**(n+1) 
    teller = 0
    
    while (b - a) > pres:
        c = (a + b) / 2
        f_c = f_d(c)
        teller += 1
        #print(c) 

        if f_a * f_c < 0:
            b = c
        else:
            a = c

    x_h = (a + b) / 2

    return x_h, n, teller
    

# Plot av f(x)
x = np.linspace(0, 20, 1000)
y = f(x)
plt.plot(x, y)
plt.title("f(x)")
plt.grid()
plt.show()
