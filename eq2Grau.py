
def xLinha(a, b, c):
    d = (b ** 2) - 4 * a * c
    xI = (-b + (d ** (1 / 2))) / 2 * a
    return xI

def x2Linhas(a, b, c):
    d = (b ** 2) - 4 * a * c
    xII = (-b - (d ** (1 / 2))) / 2 * a
    return xII


def main():

    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))



    print("O valor de X' é", xLinha(a, b, c))

    print("O valor de X'' é", x2Linhas(a, b, c))

main()

