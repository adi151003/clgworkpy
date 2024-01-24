def overloading_reverse(s):
    str = ""
    for i in s:
	    str = i + str
    return str

s =input("Enter something :")

print ("The original is : ",end="")
print (s)

print ("The reversed is : ",end="")
print (overloading_reverse(s))
