
def main():
    print(calc_position(1))


def calc_position(n_position):
    if n_position == 1:
        return "Medalla de oro"
    elif n_position == 2:
        return "Medalla de plata"
    elif n_position == 3:
        return "Medalla de bronce"
    else:
        return "Gracias por participar"


if __name__ == '__main__':
    main()

