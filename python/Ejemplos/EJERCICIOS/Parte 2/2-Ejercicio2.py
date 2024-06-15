x = 7


def main():
    if test():
        print("El factorial de {0} es {1}".format(x, zero()))
    else:
        print("El numero no cumple los requisitos (positivo y menor que 7)")


def test():
    return 0 < x < 7


def zero():
    if x == 0:
        return 1
    else:
        return factor()


def factor():
    total = 1
    for i in range(x):
        total = total * (i + 1)
    return total


if __name__ == '__main__':
    main()
