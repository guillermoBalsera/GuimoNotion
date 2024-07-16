""" Meter por teclado tu edad y la de tu compañero. Si eres 
más joven que tu compañero visualiza: "soy más joven que mi 
compañero",  en  caso  de  que  sea  tu  compañero  más  joven  
visualiza: "mi compañero es más joven que yo", y si sois de 
la misma edad: "somos de la misma edad" """

def main():
    age1 = 10
    age2 = 10
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
