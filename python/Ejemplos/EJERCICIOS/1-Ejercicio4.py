today_temperature = 20
yesterday_temperature = 21

def main():
    if today_temperature > yesterday_temperature:
        print("Hace mas calor que ayer")
    elif today_temperature < yesterday_temperature:
        print("Hace mas frio que ayer")
    else:
        print("Hace la misma temperatura que ayer")


if __name__ == '__main__':
    main()

