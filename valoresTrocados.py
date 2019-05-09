def main():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))



    print("O valor de a é: ", a, "\n", "O valor de b é: ", b)

    a = a + b
    b = a - b
    a = a - b

    print("O novo valor de a é: ", a, "\n",
          "O novo valor de b é: ", b)


main()
