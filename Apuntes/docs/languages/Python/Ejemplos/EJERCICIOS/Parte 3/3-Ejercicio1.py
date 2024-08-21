""" Una planta que fabrica perfiles de hierro posee un lote 
de n piezas. Confeccionar un programa que pida ingresar por 
teclado la cantidad de piezas a procesar y luego ingrese la 
longitud  de  cada  perfil;  sabiendo  que  la  pieza  cuya 
longitud esté comprendida en el  rango de 1,20 y 1,30 son 
aptas.  Imprimir  por  pantalla  la  cantidad  de  piezas  aptas 
que hay en el lote. """

import random


def main():
    pieces = get_random_pieces(15000)
    suitable_pieces_filter = filter(lambda x: 1.2 < x < 1.3, pieces)
    suitable_pieces = list(suitable_pieces_filter)
    suitable_pieces_length = len(suitable_pieces)
    suitable_pieces_min = min(suitable_pieces)
    suitable_pieces_max = max(suitable_pieces)
    print("Número de piezas aptas: {}".format(suitable_pieces_length))
    print("Pieza más pequeña: {}".format(suitable_pieces_min))
    print("Pieza más grande: {}".format(suitable_pieces_max))


def get_random_pieces(n_pieces):
    pieces = []
    for i in range(n_pieces):
        pieces.append(
            random.uniform(1, 2)
        )
    return pieces


if __name__ == '__main__':
    main()
