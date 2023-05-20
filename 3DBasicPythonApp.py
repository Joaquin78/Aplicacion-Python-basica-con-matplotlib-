# ------------------------------------------------------
# Aplicación Python 3.9 (64 bits) básica para mostrar elementos gráficos 2D sobre un espacio 3D,
# utilizando malla teselada triangular, con el paquete 'matplotlib'.
# @utor: Joaquín Miguel Parrilla Serrano
#-------------------------------------------------------

# Módulo de funciones matemáticas 'math' https://docs.python.org/es/3/library/math.html
from math import radians 

# Paquete 'numpy' https://numpy.org/doc/stable/reference/index.html#reference
import numpy as np 

# Paquetes 'matplotlib' https://matplotlib.org/stable/api/index
import matplotlib.pyplot as plt 
from matplotlib import cm

def main():

    # Definimos primero el tipo área de visualización 3D.
    plt.style.use('_mpl-gallery')
    
    # Declaramos las variables globales correspondientes, para el cálculo de la funciones Seno, Coseno y Tangente. 
    x = np.arange(0, radians(1800), radians(12))
    xs = np.cos(x)
    ys = np.sin(x)
    zs = np.tan(x)

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_trisurf(xs, ys, zs, vmin=zs.min() *2, cmap=cm.Blues)
    ax.set(xticklabels=[],
           yticklabels=[],
           zticklabels=[])

    # Mostramos gráficamente las funciones 2D proyectadas sobre el espacio 3D definido.
    plt.show()

main()
