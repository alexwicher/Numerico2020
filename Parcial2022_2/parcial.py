# Python 3.8.10
# Nombre -> Alex Ivan Wicher DNI -> 41263038 Laboratorio de Analisis Numerico I FAMAF
# Simplemente correr 'python3 parcial.py' en la terminal desde la carpeta que lo contiene
# Requiere matplotlib -> pip install matplotlib
# Requiere pandas -> pip install pandas
# Requiere numpy -> pip install numpy
# Requiere scipy -> pip install scipy
# PCInfo.txt contiene informacion de la maquina donde fue hecho y probado el codigo
import math

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import scipy as sp
import scipy.interpolate


# Aux

def ilagrange(xList, yList, zList):
    assert len(xList) == len(yList)

    def Li(x, i):
        l = 1
        xi = xList[i]
        for xj in xList:
            if xj != xi:
                l *= (x - xj) / (xi - xj)
        return l

    def P(x):
        p = 0
        for i, y in enumerate(yList):
            p += y * Li(x, i)
        return p

    return [P(z) for z in zList]  # Aproximaciones hechas con el polinomio interpolante.


# 1 a)

raw = pd.read_csv('irma.csv', header=None)
hr, long, lat = np.array(raw[0]), np.array(raw[1]), np.array(raw[2])

plt.scatter(long, lat, color='red', label='1)a) Data')
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.legend()
plt.show()


# 1 b)

def longitud():
    hourly = np.linspace(0, 24, 24)
    grange = ilagrange(hr, long, hourly)
    plt.scatter(hr, long, color='red', label='Data')
    plt.plot(hourly, grange, label='1)b) Grange-Longitud', color='purple')
    cubic_spline = sp.interpolate.interp1d(hr, long, kind='cubic', bounds_error=False)
    spline_data = cubic_spline(hourly)  # Aproximaciones hechas con el spline cubico.
    plt.plot(hourly, spline_data, label='1)b) Spline^3-Longitud', color='yellow')
    plt.xlabel('Hora')
    plt.ylabel('Longitud')
    plt.legend()
    plt.show()


longitud()


def latitud():
    hourly = np.linspace(0, 24, 24)
    grange = ilagrange(hr, lat, hourly)
    plt.scatter(hr, lat, color='red', label='Data')
    plt.plot(hourly, grange, label='1)b) Grange-Latitud', color='purple')
    cubic_spline = sp.interpolate.interp1d(hr, lat, kind='cubic', bounds_error=False)
    spline_data = cubic_spline(hourly)
    plt.plot(hourly, spline_data, label='1)b) Spline^3-Latitud', color='yellow')
    plt.xlabel('Hora')
    plt.ylabel('Latitud')
    plt.legend()
    plt.show()


latitud()

# 2 a)
xl = [0, 1.5, 2, 2.9, 4, 5.6, 6, 7.1, 8.05, 9.2, 10, 11.3, 12]
yl = [0.1, 0.2, 1, 0.56, 1.5, 2.0, 2.3, 1.3, 0.8, 0.6, 0.4, 0.3, 0.2]
z = 10
plt.scatter(xl, yl, label='2)a) Tierra-perfil', color='brown')
plt.xlabel('Ancho-X')
plt.ylabel('Altura-Y')
plt.legend()
plt.show()


# 2 b)

def trapecio_adaptativo(xlist, ylist):
    s = 0
    assert len(xlist) == len(ylist)
    for i in range(len(xlist) - 1):
        s += ((xlist[i + 1] - xlist[i]) / 2.0) * (ylist[i + 1] + ylist[i])
    return s


# 2 c)

res = trapecio_adaptativo(xl, yl) * 10
print(f'2)c) Para nivelar a la altura aprox. de 0 metros se removeran {math.ceil(res)} metros cubicos')
