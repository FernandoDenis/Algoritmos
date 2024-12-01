import numpy as np
import matplotlib.pyplot as plt

# Datos de duración (asegúrate de incluir la lista completa)
duracion = [
    2227, 1963, 1923, 1917, 1962, 1894, 1895, 1895, 1894, 1932, 2053, 1993, 2023, 1834, 
    4273, 1729, 1765, 3052, 1405, 1466, 1281, 3238, 1120, 1138, 1082, 1008, 1009, 953, 
    916, 917, 934, 891, 805, 825, 706, 732, 646, 633, 574, 567, 567, 514, 514, 449, 449, 
    393, 393, 399, 399, 399, 399, 399, 399, 399, 362, 431, 449, 468, 554, 573, 647, 726, 
    825, 865, 905, 916, 971, 990, 989, 1045, 1176, 1231, 1287, 1281, 1348, 1365, 1388, 
    1489, 1506, 1584, 1607, 1635, 1668, 1714, 1683, 1735, 1729, 1735, 1729, 1735, 1729, 
    1735, 1729, 1735, 1729, 1750, 1744, 1835, 1835, 1805, 1824, 1713, 1704, 3286, 1533, 
    1506, 1472, 1422, 1348, 1281, 1263, 1244, 1169, 1045, 990, 915, 971, 916, 845, 752, 
    726, 647, 672, 607, 553, 553, 547, 548, 554, 553, 547, 547, 548, 554, 548, 547, 548, 
    553, 553, 548, 547, 554, 553, 607, 666, 686, 745, 732, 845, 864, 916, 953, 1046, 
    1083, 1170, 1281, 1315, 1370, 1422, 1473, 1533, 1601, 1624, 1699, 1690, 1714, 1713, 
    1713, 1714, 1713, 1714, 1713, 1714, 1668, 1617, 1556, 1489, 1415, 1365, 1321, 1268, 
    1250, 1157, 1064, 990, 971, 845, 726, 627, 527, 418, 380, 380
]

# Definir la frecuencia de muestreo
fs = 1  # Frecuencia de muestreo en Hz (si los datos fueron tomados cada segundo)

# Calcular la Transformada de Fourier de la duración
duracion_fft = np.fft.fft(duracion)

# Calcular las frecuencias correspondientes
frecuencias = np.fft.fftfreq(len(duracion), d=1/fs)

# Calcular el espectro de fase
fase = np.angle(duracion_fft)

# Graficar el espectro de fase
plt.figure(figsize=(12, 6))
plt.plot(frecuencias[:len(frecuencias)//2], fase[:len(fase)//2])
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Fase (radianes)")
plt.title("Espectro de Fase de la Señal de Duración")
plt.grid(True)
plt.show()
