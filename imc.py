def main():

    peso = float(input("Digite seu peso: "))

    h = float(input("Digite sua altura: "))

    imc = peso / (h ** 2)

    if (imc < 18.5):

        print("Abaixo do peso!")

    elif (imc >= 18.5 and imc < 25):

        print("Peso normal!")

    elif (imc >= 25 and imc < 30):

        print("Acima do peso!")

    else:

        print("Obeso!")

main()