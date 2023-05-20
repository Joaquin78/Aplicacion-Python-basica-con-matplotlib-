# ------------------------------------------------------
# Aplicación Python 3.9 (64 bits) básica para mostrar elementos gráficos 2D,
# con el paquete 'matplotlib'.
# @utor: Joaquín Miguel Parrilla Serrano
#-------------------------------------------------------

# Módulo de funciones matemáticas 'math' https://docs.python.org/es/3/library/math.html
from math import radians 

# Paquete 'numpy' https://numpy.org/doc/stable/reference/index.html#reference
import numpy as np 

# Paquete 'matplotlib' https://matplotlib.org/stable/api/index
import matplotlib.pyplot as plt 

def main():
    x = np.arange(0, radians(1800), radians(12))
    # Calculamos la función Coseno, pasando los párametros formales antes declarados
    plt.plot(x, np.cos(x), 'b')
    # Mostramos gráficamente la función Coseno antes implementada
    plt.show()

main()