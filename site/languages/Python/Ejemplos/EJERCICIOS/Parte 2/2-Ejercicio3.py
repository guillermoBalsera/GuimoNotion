""" Hacer un programa que nos permita introducir un año y un 
mes  por  el  teclado  (introducirlo  en  formato  numérico: 
enero=1, febrero=2....), validarlo para que esté comprendido 
entre 1 y 12, y visualizar por pantalla los días que tiene 
el mes. 
 
NOTA: Recordar que febrero puede ser bisiesto (buscar por 
internet cuándo un mes es bisiesto). """


def main():
    month = 5
    year = 2024
    print(calc_month(month, year))


def calc_month(month, year):
    if month == 1:
        return 31
    elif month == 2:
        return february(year)
    elif month == 3:
        return 31
    elif month == 4:
        return 30
    elif month == 5:
        return 31
    elif month == 6:
        return 30
    elif month == 7:
        return 31
    elif month == 8:
        return 31
    elif month == 9:
        return 30
    elif month == 10:
        return 31
    elif month == 11:
        return 30
    elif month == 12:
        return 31


def february(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return 29
    else:
        return 28


if __name__ == '__main__':
    main()
