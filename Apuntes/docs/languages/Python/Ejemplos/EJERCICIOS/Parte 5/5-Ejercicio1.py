""" Hacer un programa que calcule un número de la serie Fibonacci indicándole la 
posición  de ese número. 
Un número de la serie Fibonacci se calcula sumando los dos números 
anteriores a él,  siendo los dos primeros cero y uno. Esta es la serie Fibonacci: 0, 
1, 1, 2, 3, 5, 8, 13, 21 ... 
Ejm: El número  que está en la posición 6 sería el 5. """

def main():
    position = 6
    run(position)
    print(run_2(position))


def run(position):
    x = position - 2
    p1 = 0
    p2 = 1
    print("{} ".format(0))
    print("{} ".format(1))
    while x > 0:
        calc = p2 + p1
        p1 = p2
        p2 = calc
        print("{} ".format(calc))
        x = x - 1


def run_2(position):
    secuence = [0, 1]
    while len(secuence) < position:
        secuence.append(
            secuence[-1] + secuence[-2]
        )
    return secuence


if __name__ == "__main__":
    main()
