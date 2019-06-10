def main():

    sexo = input("Digite o sexo: \n(M) Masculino \n(F) Femenino \n ")

    altura = float(input("Digite sua altura: "))

    if (sexo == "M"):

        print("Seu peso ideal é: ", (72.7 * altura) - 58)

    else:

        print("Seu peso ideal é: ", (62.1 * altura) - 44.7)

main()
