""" Meter un número desde el teclado, si es uno, sacar por 
pantalla: "El número es uno"; si es dos, sacar por pantalla 
"el número es dos", y si es cualquier otro número sacar por 
pantalla: "es otro número distinto de uno y dos" """


def main():
    x = 1
    if x == 1:
        print("El numero es uno")
    elif x == 2:
        print("El numero es dos")
    else:
        print("EL numero no es ni uno ni dos")


if __name__ == "__main__":
    main()
