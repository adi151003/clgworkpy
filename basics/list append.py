list=[]
print ("initial blank list: ")
print (list)
n=int(input("enter number of terms to be inserted: "))
for i in range(1,n+1):
    a=int(input("enter the value: "))
    list.append(a)    
print ("\nlist after addition of the elements: ")
print(list)
total=0
for a in range(0,len(list)):
    total=total+list[a]
print("sum of all elements in the list is :", total)