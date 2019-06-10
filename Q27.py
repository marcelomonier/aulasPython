def main():

    list1 = [1, 2, 3]

    list2 = [4, 5, 6]

    list3 = []

    for Elemlist1, Elemlist2 in zip(list1, list2):

        list3.append((Elemlist1 + Elemlist2))

    print(list3)

main()