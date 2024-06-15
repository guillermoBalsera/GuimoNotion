n = 6


def main():
    print("Suma de totales: {}".format(calculate_sum()))
    print("Suma de pares: {}".format(calculate_even()))
    print("Suma de impares: {}".format(calculate_odd()))


def calculate_sum():
    total = 0
    for i in range(n):
        total += i
    return total


def calculate_even():
    total = 0
    for i in range(n):
        if i % 2 == 0:
            total += i
    return total


def calculate_odd():
    total = 0
    for i in range(n):
        if i % 2 != 0:
            total += i
    return total


if __name__ == '__main__':
    main()
