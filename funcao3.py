import calculadora

def main():

    x = float(input("Digite um número: "))

    y = float(input("Digite outro número: "))

    print(calculadora.soma(x, y))

    print(calculadora.multi(x, y))

    print(calculadora.subt(x, y))

    print(calculadora.divi(x, y))

main()