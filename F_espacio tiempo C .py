import numpy as np
import matplotlib.pyplot as plt

# Velocidad de la luz
c = 299792.4583  # km/s

# Velocidades
v = np.linspace(0, c, 500)

# Tiempo relativo
t = np.sqrt(1 - (v**2 / c**2))

# -----------------------------
# Punto 1: tiempo relativo para v = 0.5c
# -----------------------------
v1 = 0.5 * c
t1 = np.sqrt(1 - (v1**2 / c**2))

# -----------------------------
# Punto 2: velocidad para t = 0.5
# t = sqrt(1 - v²/c²)
# => v = c * sqrt(1 - t²)
# -----------------------------
t2 = 0.5
v2 = c * np.sqrt(1 - t2**2)

# -----------------------------
# -----------------------------
# Punto 3: Cálculo del Radio de Curvatura Real (Espacio-Tiempo)
# -----------------------------
# Al proyectar el espacio de fases a una métrica geométrica usando 1 segundo de referencia:
radio_curvatura_km = c                     # R = 299792.4583 km
curvatura_plano_km2 = 1 / (radio_curvatura_km**2) # k = 1.11265e-11 km⁻²

radio_curvatura_m = radio_curvatura_km * 1000     # R = 299792458.3 metros
curvatura_plano_m2 = 1 / (radio_curvatura_m**2)   # k = 1.11265e-17 m⁻²


# Crear figura
plt.figure(figsize=(9,6))

# Curva principal
plt.plot(t, v, color='blue', label='Relación relativista')

# Marcar punto v = 0.5c
plt.scatter(t1, v1, color='red', s=80)
plt.annotate(
    f'v = 0.5c\n t = {t1:.3f}',
    (t1, v1),
    textcoords="offset points",
    xytext=(-80,20),
    arrowprops=dict(arrowstyle='->')
)

# Marcar punto t = 0.5
plt.scatter(t2, v2, color='green', s=80)
plt.annotate(
    f't = 0.5\n v = {v2:.0f} km/s',
    (t2, v2),
    textcoords="offset points",
    xytext=(20,-40),
    arrowprops=dict(arrowstyle='->')
)

# Etiquetas
plt.xlabel('Tiempo relativo')
plt.ylabel('Velocidad (km/s)')

# Título
plt.title('Tiempo relativo vs Velocidad')

# Cuadrícula
plt.grid(True)

# Leyenda
plt.legend()

# Mostrar
plt.show()
