def soma(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def divi(x, y):
    return x / y

def main():

    x = float(input("Digite um número: "))
    y = float(input("Digite outro número: "))

    print(soma(x, y))
    print(sub(x, y))
    print(mult(x, y))
    print(divi(x, y))

main()