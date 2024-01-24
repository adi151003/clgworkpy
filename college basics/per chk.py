a = int(input("Enter your percentage : "))
print("Your percentage is",a)
if 85<=a<= 100:
    print("You got A+ grade")
elif 70<=a<=84 :
    print("You got A grade")
elif 60<=a<=69 :
    print("You got B+ grade")
elif 50<=a<=59 :
    print("You got B grade")
elif 40<=a<=49 :
    print("You got C grade")
elif 40<=a<=0:
    print("you got F grade")
else:
    print("enter correct percentage")
