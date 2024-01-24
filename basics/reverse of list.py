def Reverse(lst):
    lst.reverse()
    return lst

lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
print ("original list is : ",lst)
print("reversed list is : ",Reverse(lst))