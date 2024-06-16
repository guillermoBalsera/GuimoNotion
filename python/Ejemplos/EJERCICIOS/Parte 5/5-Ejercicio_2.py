def main():
    number = 5387442310523874913
    numbers = odd_digits(number)
    if len(numbers) > 0:
        print("El numero contiene numeros impares: ")
        print(numbers)
    else:
        print("El numero no tiene impares")
    numbers = odd_digits2(number)
    if len(numbers) > 0:
        print("El numero contiene numeros impares: ")
        print(numbers)
    else:
        print("El numero no tiene impares")


def odd_digits(number):
    number_length = len(str(number))
    numbers = ""
    while number_length > 0:
        rest = number % 10
        number = number / 10
        if rest % 2 != 0:
            numbers = "{0} {1}".format(numbers, rest  )
        number_length = number_length - 1

    return numbers


def odd_digits2(number):
    str_number = str(number)
    split_number = list(str_number)
    mapped_numbers = map(int, split_number)
    odds = filter(lambda x: x % 2 != 0, mapped_numbers)
    odds = set(odds)
    return odds


if __name__ == '__main__':
    main()
