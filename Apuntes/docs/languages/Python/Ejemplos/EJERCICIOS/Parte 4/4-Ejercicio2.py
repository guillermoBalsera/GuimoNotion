""" Hacer  un  programa  que  nos  permita  leer  un  número  por  el  teclado  que 
represente el  precio  de  un  producto,  y  calcule  el  precio final  del  mismo  con el 
IVA incluido. El IVA será el 21%. """


def main():
    money = 20
    print("{}€ IVA incluido".format(calc_total(money)))


def calc_total(money):
    return money + money * 21 / 100


if __name__ == "__main__":
    main()
