import numpy as np
import matplotlib.pyplot as plt


# Funksjonen f(x) og f´(x)
def f(x):
    return np.exp(-x/4) * np.arctan(x)

def f_derivert(x):
    pass



# Plot av f(x)
x = np.linspace(0, 10, 100)
y = f(x)
plt.plot(x, f(x))
plt.grid()
plt.show()