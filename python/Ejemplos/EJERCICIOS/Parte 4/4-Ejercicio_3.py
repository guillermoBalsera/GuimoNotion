import math
import random


def main():
    c1 = random_number()
    c2 = random_number()
    print("La hipotenusa de un triangulo recatangulo con catetos {0} y {1} es {2}".format(
        c1, c2, calc_hip(c1, c2)
    ))


def random_number():
    return random.randint(1, 50)


def calc_hip(c1, c2):
    calc1 = math.pow(c1, 2)
    calc2 = math.pow(c2, 2)
    total = calc1 + calc2
    return math.sqrt(total)


if __name__ == "__main__":
    main()
