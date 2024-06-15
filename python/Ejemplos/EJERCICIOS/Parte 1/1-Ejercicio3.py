

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
