num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
num3=int(input("Enter a number:"))
num4=int(input("Enter a number:"))
num5=int(input("Enter a number:"))
if (num1>num2 and num1>num3 and num1>num4 and num1>num5):
    print("Number 1 is greatest")
elif (num2>num1 and num2>num3 and num2>num4 and num2>num5): 
    print("Number 2 is greatest")
elif (num3>num1 and num3>num2 and num3>num4 and num3>num5):
    print("Number 3 is greatest")
elif (num4>num1 and num4>num2 and num4>num3 and num4>num5):
    print("Number 4 is greatest")
else:
    print("Number 5 is greatest")