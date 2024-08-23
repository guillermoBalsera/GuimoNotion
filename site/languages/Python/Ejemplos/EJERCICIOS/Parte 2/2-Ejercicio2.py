""" Calcular el factorial de un número positivo menor que 7 
(validar por programa). 
 
NOTA:  EL  factorial  de  un  número  cualquiera  se  calcula 
multiplicando desde 1 hasta el mismo número. Por ejemplo: 
5! = 1*2*3*4*5 = 120. 
El factorial de cero es siempre 1. """

def main():
    x = 7
    if test():
        print("El factorial de {0} es {1}".format(x, zero(x)))
    else:
        print("El numero no cumple los requisitos (positivo y menor que 7)")


def test(x):
    return 0 < x < 7


def zero(x):
    if x == 0:
        return 1
    else:
        return factor()


def factor(x):
    total = 1
    for i in range(x):
        total = total * (i + 1)
    return total


if __name__ == '__main__':
    main()
