"""  Hacer  un  programa  que  nos  permita  meter  por  el teclado 
un  valor  “n”  positivo  entre  1  y  20  (validarlo  mediante 
programa).  Calcular  la  suma  de  los  “n”  primeros  números 
naturales, la suma de los números pares, los impares y los 
cuadrados. Finalmente mostrar resultados en pantalla.  """

def main():
    n = 6
    print("Suma de totales: {}".format(calculate_sum(n)))
    print("Suma de pares: {}".format(calculate_even(n)))
    print("Suma de impares: {}".format(calculate_odd(n)))


def calculate_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total


def calculate_even(n):
    total = 0
    for i in range(n):
        if i % 2 == 0:
            total += i
    return total


def calculate_odd(n):
    total = 0
    for i in range(n):
        if i % 2 != 0:
            total += i
    return total


if __name__ == '__main__':
    main()
