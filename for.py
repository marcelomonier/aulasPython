def main():

    lisPar = []
    listImpar = []

    for x in range(1, 101):

        if x % 2 == 0:
            lisPar.append(x)
        else:
            listImpar.append(x)

    print(lisPar)
    print(listImpar)




main()