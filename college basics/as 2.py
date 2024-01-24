m1=float (input("enter marks of first subject:  "))
m2=float(input("enter marks of second subject:  "))
m3=float(input("enter marks of third subject:  "))
m4=float(input("enter marks of fourth subject:  "))
m5=float(input("enter marks of fifth subject:  "))
p= None
p=((m1+m2+m3+m4+m5)/500)*100
print ("the percentage is:  \n",p)
if (p>=85):
    print ("the grade is A+")
elif (p>=70 and p<=84):
    print ("the grade is A")
elif (p>=60 and p<=69):
    print ("the grade is B+")   
elif (p>=50 and p<=59):
    print ("the grade is B")
elif (p>=40 and p<=49):
    print ("the grade is C")
elif (p<40):
    print ("the grade is F")
else :
    print("enter correct marks")
