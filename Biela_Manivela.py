import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import os
print("Directorio actual:", os.getcwd())


# Parámetros del sistema
r = 5  # Longitud de la manivela
l = 15  # Longitud de la biela
omega = 2 * np.pi  # Velocidad angular (rad/s)
fps = 20  # Frames por segundo
T = 2  # Duración de la simulación en segundos

# Función para calcular la posición del pistón
def calculate_piston_position(theta):
    x = r * np.cos(theta) + np.sqrt(l**2 - (r * np.sin(theta))**2)
    return x

# Configuración de la simulación
t = np.linspace(0, T, fps * T)  # Tiempo discretizado
theta = omega * t  # Ángulo de la manivela
x = calculate_piston_position(theta)  # Posición del pistón

# Configuración de la gráfica
fig, ax = plt.subplots()
# Limites de la gráfica
ax.set_xlim(-r-2, r+l+2) 
ax.set_ylim(-r-2, r+2)

# Elementos gráficos
manivela_line, = ax.plot([], [], 'o-', lw=2, label="Manivela")
biela_line, = ax.plot([], [], 'o-', lw=2, label="Biela")
piston, = ax.plot([], [], 'ks', ms=10, label="Pistón")

# Inicialización de la animación
def init():
    manivela_line.set_data([], [])
    biela_line.set_data([], [])
    piston.set_data([], [])
    return manivela_line, biela_line, piston

# Función de animación
def update(frame):
    # Posiciones
    theta = omega * frame / fps
    crank_x = r * np.cos(theta)
    crank_y = r * np.sin(theta)
    piston_x = calculate_piston_position(theta)

    # Actualizar elementos
    manivela_line.set_data([0, crank_x], [0, crank_y])
    biela_line.set_data([crank_x, piston_x], [crank_y, 0])
    piston.set_data([piston_x], [0])
    return manivela_line, biela_line, piston

# Crear la animación
anim = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=1000 / fps)

# Mostrar la animación
plt.legend()
plt.title("Simulación del sistema biela-manivela")
plt.xlabel("Rad")
plt.ylabel("metros")
plt.grid()
plt.show()

anim.save('biela_manivela.gif', writer='imagemagick', fps=30)