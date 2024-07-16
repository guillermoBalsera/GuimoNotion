""" Hacer  un  programa  que  convierta  una  cantidad  de  euros  introducida  por 
teclado a dólares, yenes o libras, sabiendo que: 
 
1 euro son 0,87 libras. 
    1 euro son 1,11 dólares. 
      1 euro son 120,63 yenes. 
 
El programa parará cuando metamos la cadena "fin"  """

import random


def main():
    option = get_option()
    money = get_money()
    result = run(option, money)
    option_name = get_option_name(option)
    print("{0}€ son {1} {2}".format(money, result, option_name))


def get_money():
    return random.randint(0, 1000)


def get_option():
    return random.randint(1, 3)


def get_option_name(option):
    if option == 1:
        return "libras"
    elif option == 2:
        return "dolares"
    else:
        return "yenes"


def run(option, money):
    if money == 0:
        return "Fin de programa"
    else:
        return convert(option, money)


def convert(option, money):
    if option == 1:
        return convert_to_pounds(money)
    elif option == 2:
        return convert_to_dolars(money)
    else:
        return convert_to_yens(money)


def convert_to_pounds(money):
    return money * 0.87


def convert_to_dolars(money):
    return money * 1.11


def convert_to_yens(money):
    return money * 120.63


if __name__ == "__main__":
    main()
