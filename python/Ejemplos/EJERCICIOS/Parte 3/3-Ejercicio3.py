""" Calcula  las  raíces  reales  de  una  ecuación  de  segundo 
grado: aX2+bX+c=0.Si no existen raíces reales indicarlo por 
pantalla. 
Nota:  Buscar  que  método  de  la  clase  Math  nos  permite 
calcular una raíz cuadrada """

import math


def main():
    a1, b1, c1 = 0, 0, 0
    a2, b2, c2 = 0, 0, 1
    a3, b3, c3 = 0, 2, 4
    a4, b4, c4 = 1, -3, 2

    resultados = [
        run(a1, b1, c1),
        run(a2, b2, c2),
        run(a3, b3, c3),
        run(a4, b4, c4)
    ]

    for i, resultado in enumerate(resultados):
        print(f"Ejemplo {i+1}: {resultado}")


def run(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "La ecuación tiene infinitas soluciones (identidad)"
            else:
                return "La ecuación no tiene solución (inconsistencia)"
        else:
            x = -c / b
            return f"La ecuación es lineal y tiene una solución: {x}"
    else:
        discriminante = b ** 2 - 4 * a * c
        if discriminante < 0:
            return "No existen raices reales"
        elif discriminante == 0:
            raiz_real = -b / (2 * a)
            return f"Solo existe una raíz real: {raiz_real}"
        else:
            return calc_roots(a, b, c)


def calc_roots(a, b, c):
    sqrt = math.sqrt(b ** 2 - 4 * a * c)
    x = (-b + sqrt) / (2 * a)
    y = (-b - sqrt) / (2 * a)
    return "Las raíces son {0} y {1}".format(x, y)


if __name__ == "__main__":
    main()
