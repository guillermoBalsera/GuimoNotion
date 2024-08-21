""" Supón que estuviste en las Olimpiadas de Río de Janeiro, 
y  que  participaste  en  la  prueba  de  los  100  metros  lisos. 
Introduce por el teclado un número que haga referencia al 
puesto  en  el  que  quedaste.  Utilizando  la  instrucción 
switch,  visualiza  el  medallero  (medalla  de  oro  (primer 
puesto),  plata  (segundo  puesto),  bronce  (tercer  puesto), 
gracias por participar (cualquier otro puesto). """

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

