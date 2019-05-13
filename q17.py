def soma(x, y):
    return x + y

def subtração(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y

def main():

    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))

    operacao = int(input("Escolha uma das opções abaixo: \n 1 - Soma \n "
                         "2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n: "))



    if operacao == 1:
        print(soma(num1, num2))
    elif operacao == 2:
        print(subtração(num1, num2))
    elif operacao == 3:
        print(multiplicacao(num1, num2))
    elif operacao == 4:
        print(divisao(num1, num2))
    else:
        print("Escolha uma das opções!")


main()
