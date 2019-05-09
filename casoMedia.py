def main():
    a = int(input("Digite a primeira nota: "))
    b = int(input("Digite a segunda nota: "))
    c = int(input("Digite a terceira nota: "))

    d = (a + b + c) / 3

    if d >= 7:
        print("Aluno aprovado")
    else:
        print("Aluno reprovado")

main()
