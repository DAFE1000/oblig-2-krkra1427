import numpy as np
import matplotlib.pyplot as plt

# Funksjonen f(x) og dens deriverte
def f(x):
    return np.exp(-x/4) * np.arctan(x)

def f_d(x):
    return -np.exp(-x/4)/4 * (np.arctan(x) - (4 / (1 + x**2)))

def halveringsmetode(a, b, n):
    """ Halveringsmetoden for løsning av likning på formen f(x)=0. 
    Inputs (startverdier): a og b velges hvor f(a) og f(b) har motsatt fortegn.
    n: antall desimaler som ønskes med sikkerhet i svaret """
    
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
    

# Plot
x = np.linspace(-1, 5, 1000) 
funk = f(x)
funk_d = f_d(x)

plt.plot(x, funk, color='blue')
plt.plot(x, funk_d, color='red')
plt.title("f(x) og f´(x)")
plt.grid()
plt.show()


# Utskrift av svar med halveringsmetode samt plot
def main ():

    x_h, n, teller = halveringsmetode(-1, 2, 4)
    print(f"Halveringsmetoden: toppunkt x = {x_h:.{n}f}, y = {f(x_h):.{n}f}. Antall iterasjoner: {teller}")   

if __name__ == "__main__":
    main()
