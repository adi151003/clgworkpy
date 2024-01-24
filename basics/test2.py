def integer_check():
    while True:
        try:
             a = int(input("Enter something: "))
        except ValueError:
            print("Not an integer!")
            break
        else:
            print("Yes an integer!")
            break 
def float_check():
    while True:
        try:
             b = float(input("Enter something: "))
        except ValueError:
            print("Not a float!")
            break
        else:
            print("Yes a float!")
            break
integer_check()
float_check()