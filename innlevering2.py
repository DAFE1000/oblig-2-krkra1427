import numpy as np
import matplotlib.pyplot as plt

# Oppgave: En funksjon f(x) har et maksimalpunkt. 
# Bestem topp punkt med fire rette desimaler. 
# Plott funksjonen og markér toppunktet du fann i dette plottet.

# Funksjonen f(x) og dens deriverte f´(x)
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
    

def main ():
# Utskrift av svar med halveringsmetode
# plot av f(x), f´(x) og toppunkt til f(x) (f´(x)=0) funnet med halveringsmetoden

    x_h, n, teller = halveringsmetode(-1, 2, 4)
    print(f"Halveringsmetoden: toppunkt x = {x_h:.{n}f}, y = {f(x_h):.{n}f}. Antall iterasjoner: {teller}")   
  
    x = np.linspace(-1, 5, 1000) 
    funk = f(x)
    funk_d = f_d(x)
    
    plt.plot(x, funk, color='blue')
    plt.plot(x, funk_d, color='red')
    plt.plot(x_h, f(x_h), 'rx', markersize=5, fillstyle='none')

    # Rutenett, tittel
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.grid(visible=True)
    plt.title("f(x) og f´(x)")
    plt.show()


if __name__ == "__main__":
    main()

