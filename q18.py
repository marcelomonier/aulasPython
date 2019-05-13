def extenso(num):


    list2 = ["Um", "Dois", "Três", "Quatro", "Cinco", "Seis",
             "Sete", "Oito", "Nove", "Dez"]


    if num == 1:
        print(list2[0])
    elif num == 2:
        print(list2[1])
    elif num == 3:
        print(list2[2])
    elif num == 4:
        print(list2[3])
    elif num == 5:
        print(list2[4])
    elif num == 6:
        print(list2[5])
    elif num == 7:
        print(list2[6])
    elif num == 8:
        print(list2[7])
    elif num == 9:
        print(list2[8])
    elif num == 10:
        print(list2[9])
    else:
        print("Número inválido")

    return num
def main():

    num = int(input("Digite um número: "))
    print(extenso(num))

main()
