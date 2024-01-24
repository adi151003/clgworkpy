def sum():
    d=int(input("Enter no. of values you need to add"))
    total=0
    x=[]
    for i in range(d):
        ele = int(input("Enter number"))
        x.append(ele)  	
        print (x)
    for ele in range(0, len(x)):
        total = total + x[ele]


def sub():
    a = int(input("enter no. 1 : "))
    b = int(input("enter no. 2 : "))
    return a-b


def multiply():
    a = int(input("enter no. 1 : "))
    b = int(input("enter no. 2 : "))
    return a*b


def div():
    a = int(input("enter no. 1 : "))
    b = int(input("enter no. 2 : "))
    return a/b


def screen():
    print("Simple calculator by Aditya\n")
    print("enter 1 for sum")
    print("enter 2 for subtraction")
    print("enter 3 for multiply")
    print("enter 4 for division")
    c = int(input("Enter what you want to do : "))
    if c == 1:
        print("the answer is:\n", sum())
        d = int(input("Enter 1 to continue or 2 to exit"))
        while d == 1:
            screen()
    elif c == 2:
        print("the answer is:\n", sub())
        d = int(input("Enter 1 to continue or 2 to exit"))
        while d == 1:
            screen()
    elif c == 3:
        print("the answer is:\n", multiply())
        d = int(input("Enter 1 to continue or 2 to exit"))
        while d == 1:
            screen()
    elif c == 4:
        print("the answer is:\n", div())
        d = int(input("Enter 1 to continue or 2 to exit"))
        while d == 1:
            screen()
    else:
        print("Wrong input")
        screen()


screen()