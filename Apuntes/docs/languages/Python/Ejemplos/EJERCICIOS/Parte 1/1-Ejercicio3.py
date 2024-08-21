""" Introducir  por  el  teclado  la  presión  que  tiene  nuestra  
caldera  de  la  calefacción  (debe  ser  de  tipo  float)  y  
almacenarla  en  una  variable  que  llamaremos  presión.  Si  
sobrepasa el valor de 2 hacer: 
a) Visualizar por pantalla: Abrir válvula de seguridad. 
b) Disminuir en uno el valor de presión. 
En el caso de que no sobrepase el valor de dos hacer: 
a) introducir tu nombre por teclado. 
b) Imprimir: "Todo está bien [tu nombre]. """

def main():
    pressure = 0.3
    pressure = pressure_control(pressure)
    print(pressure)


def pressure_control(presure):
    if presure > 2:
        print("Abrir valvula de seguridad")
        return presure - 1
    else:
        print("Todo esta bien")
        return presure


if __name__ == "__main__":
    main()
