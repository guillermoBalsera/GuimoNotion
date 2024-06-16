
def main():
    money = 20
    print("{}€ IVA incluido".format(calc_total(money)))


def calc_total(money):
    return money + money * 21 / 100


if __name__ == "__main__":
    main()
