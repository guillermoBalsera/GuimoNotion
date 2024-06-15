age1 = 10
age2 = 10


def main():
    calculate_older(age1, age2)


def calculate_older(age1, age2):
    if age1 > age2:
        print("La persona 1 es la mayor")
    elif age1 < age2:
        print("La persona 2 es la mayor")
    else:
        print("Tienen la misma edad")


if __name__ == "__main__":
    main()
