x = 10

def main():
    piramid()

def piramid():
    for i in range(x):
        for j in range(x-i):
            print(" ", end="")
        for k in range(2*i+1):
            print("*", end="")
        print()

if __name__ == "__main__":
    main()
