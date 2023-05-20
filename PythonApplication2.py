# ------------------------------------------------------
# Aplicación Python 3.9 (64 bits) básica para mostrar elementos gráficos 2D,
# con el paquete 'matplotlib'.
#-------------------------------------------------------

# Módulo de funciones matemáticas 'math' https://docs.python.org/es/3/library/math.html
from math import radians 

# Paquete 'numpy' https://numpy.org/doc/stable/reference/index.html#reference
import numpy as np 

# Paquete 'matplotlib' https://matplotlib.org/stable/api/index
import matplotlib.pyplot as plt 

def main():
    # Declaramos la variable local 'x', asignándola la función 'arange' instanciada de np.
    x = np.arange(0, radians(1800), radians(12))
    
    # Calculamos la función Seno y Coseno, pasando como parámetro formal la variable local 'x' antes declarada.
    plt.plot(x, np.cos(x), np.sin(x), 'b')
 
    # Mostramos gráficamente las funciones Seno y Coseno.
    plt.show()

main()
