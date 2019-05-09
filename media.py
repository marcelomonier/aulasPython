def main():
    a = int(input("Digite a primeira nota: "))
    b = int(input("Digite a segunda nota: "))
    d = int(input("Digite a terceira nota: "))

    c = (a + b + d) / 3

    if c >= 7:
        print("Aluno aprovado - ", c)
    else:
        print("Aluno reprovado - ", c)



main()