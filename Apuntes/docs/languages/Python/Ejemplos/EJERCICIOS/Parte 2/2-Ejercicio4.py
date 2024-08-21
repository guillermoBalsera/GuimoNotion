""" Crear un programa que calcule los divisores de un número 
natural cualquiera. También mostrar si el número ingresado 
es primo. Un número primo es aquel que solo sea divisible 
por 1 y por el mismo número. """


def main():
    divisors = calculate_divisors(14)
    if len(divisors) == 2:
        print("El numero es primo")
    else:
        print("El numero no es primo y tiene {0} divisores: \n{1}".format(len(divisors), divisors))


def calculate_divisors(n):
    divisors = [1, n]
    for i in range(2, n):
        if n % i == 0:
            divisors.append(i)
    return sorted(divisors)


if __name__ == '__main__':
    main()
