n1 = int(input("Enter first number: "))

n2 = int(input("Enter second number: "))

n3 = int(input("Enter Third number: "))


def max_of_3():
    if (n1 >= n2) and (n1 >= n3):
        l = n1

    elif (n2 >= n1) and (n2 >= n3):
        l = n2
    else:
        l = n3
    print("Largest number among the three is", l)


max_of_3()