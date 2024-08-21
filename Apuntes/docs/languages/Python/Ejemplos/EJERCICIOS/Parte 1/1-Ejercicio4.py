""" Meter por el teclado la temperatura de ayer y hoy y si 
hoy llueve o luce el sol. Hacer un programa que haga: 
a) Si la temperatura hoy es mayor de 20 grados y llueve:  
- Sacar por pantalla: "Hace calor pero está 
lloviendo". 
- Entre ayer y hoy la temperatura fue de: (sacar la 
suma de la temperatura de ayer y hoy). 
- Mañana habrá (suma 5 grados a la temperatura de 
hoy y saca el resultado por pantalla). 
 
b) Si la temperatura de hoy es menor o igual a 20 grados: 
- Sacar por pantalla: "Parece que llega el otoño". 
- Si además luce el sol visualizar: "Pero luce el 
sol", en caso contrario visualizar: "y llueve". """

def main():
    today_temperature = 20
    yesterday_temperature = 21
    if today_temperature > yesterday_temperature:
        print("Hace mas calor que ayer")
    elif today_temperature < yesterday_temperature:
        print("Hace mas frio que ayer")
    else:
        print("Hace la misma temperatura que ayer")


if __name__ == '__main__':
    main()

