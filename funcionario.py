def main():

    nome = input("Digite o nome do funcionário: ")

    qtdCarros = int(input("Digite a quantidade de carros vendidos: "))

    carro = 30000

    salario = 2000

    comissaoVendaTotal = (qtdCarros * carro) * 0.05 + salario

    print("O salário desse mês do funcionário ",nome, "é de", comissaoVendaTotal)


main()