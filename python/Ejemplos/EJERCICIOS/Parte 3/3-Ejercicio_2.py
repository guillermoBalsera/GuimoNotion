import random


def main():
    while True:
        number = random_number()
        if number == 0:
            print("FIN")
            break
        else:
            print(run(number))


def higher_number(x):
    return x > 8


def calc_double(x):
    return x * 2


def calc_triple(x):
    return x * 3


def run(number):
    if higher_number(number):
        return "{0} * 2 = {1}".format(number, calc_double(number))
    else:
        return "{0} * 3 = {1}".format(number, calc_triple(number))


def random_number():
    return random.randint(0, 10)


if __name__ == '__main__':
    main()
