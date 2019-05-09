def somarNumeros(x, y):
    return x + y

def multiplicarNumeros(x, y):
    return x * y

def subtrairNumeros(x, y):
    return x - y

def dividirNumeros(x, y):
    return x / y

def main():

    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))

    print("A soma dos números é", somarNumeros(a, b))
    print("A multiplicação dos números é", multiplicarNumeros(a, b))
    print("A subtração dos números é", subtrairNumeros(a, b))
    print("A divisão dos números é", dividirNumeros(a, b))


main()