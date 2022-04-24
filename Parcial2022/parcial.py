# Nombre -> Alex Ivan Wicher DNI -> 41263038 Laboratorio de Analisis Numerico FAMAF
# Python 3.8.10
#
#
#

import math

from matplotlib import pyplot as plt


# Aux

def funcion_numpy(I, dist):
    a, b = I
    res = [a]
    aux = a
    while aux <= b:
        aux += dist
        res.append(aux)
    return res


def f_inner(x, i):
    return ((pow(-1, i)) / math.factorial(2 * i + 1)) * pow(x, 2 * i + 1)


# 1)

def terminos_taylor(n):
    res = "0"
    for i in range(0, n):
        first = ((pow(-1, i)) / math.factorial(2 * i + 1))
        exp = 2 * i + 1
        res += ' + ' + "{:e}".format(first) + ' * X^(' + "{:e}".format(exp) + ')'
    print(res + '\n')


print('EJERCICIO 1 \n')

terminos_taylor(5)


# 2)

def graf_funcion_f(I, fun):
    x_list = funcion_numpy(I, 0.01)
    y_list = [fun(a) for a in x_list]
    plt.plot(x_list, y_list)
    plt.plot(x_list, [math.sin(c) for c in x_list])  # sin(x) para mirar
    plt.plot(x_list, [0 for c in x_list])  # para ver las raises , eligo [2.5;3.5] y [4.5;5.5]  para 3)
    plt.show()


print('EJERCICIO 2 (grafico) \n')

graf_funcion_f((0, 6.4), lambda x: math.fsum([f_inner(x, b) for b in range(0, 5)]))


# 3)


def biseccion(fun, I, err, mit):
    a, b = I
    hx, hf = [], []
    for i in range(mit):
        c = (a + b) / 2
        hx.append(c)
        hf.append(fun(c))
        if abs(fun(c)) < err:
            break
        if fun(a) * fun(c) < 0:
            b = c
        elif fun(a) * fun(c) > 0:
            a = c
        elif fun(a) * fun(b) > 0:
            break
    print('Resultado c -> ', str(hx[len(hx) - 1]), ' f(c) -> ', str(hf[len(hf) - 1]), '\n')
    return hx, hf


print('EJERCICIO 3 \n')
biseccion(lambda x: math.fsum([f_inner(x, b) for b in range(0, 5)]), (2.5, 3.5), 1e-5, 100)
biseccion(lambda x: math.fsum([f_inner(x, b) for b in range(0, 5)]), (4.5, 5.5), 1e-5, 100)
graf_funcion_f((0, 6.4), lambda x: math.fsum([f_inner(x, b) for b in range(0, 5)]))

# 4)

print('EJERCICIO 4 mirar codigo \n')


def rsteffensen(fun, x0, err, mit):
    hx, hf = [], []
    x_n = x0
    x_n_p = 0

    for k in range(mit):
        fx = fun(x_n) # Ya no hay derivada ahora
        hx.append(x_n)
        hf.append(fx)
        if abs(fx) < abs(err):
            break
        abs_x_n = abs(x_n - x_n_p)
        if x_n != 0 and (abs_x_n / abs(x_n)) < abs(err):
            break
        x_n_p = x_n
        x_n = x_n - pow(fx, 2) / (fun(x_n + fx) - fx) # Steffensen aca
    return hx, hf


# 5)

def serie_seno(x, mit, tol):
    res = 0
    for i in range(0, mit):
        res += f_inner(x, i)
        # print("Iteracion -> ", str(i), " Resultado -> ", str(res), " \n")
        if i != 0 and math.fabs(res - f_inner(x, i - 1)) < tol:
            print("Tolerancia -> ", str(tol), " alcanzada.\n")
            break

    print("Resultado -> ", str(res), " Iteraciones -> ", str(mit), " Real -> ", str(math.sin(x)), " \n")


print('EJERCICIO 5 \n')

serie_seno(3, 100, 1e-5)
serie_seno(6, 100, 1e-5)
serie_seno(4.5, 100, 1e-5)
