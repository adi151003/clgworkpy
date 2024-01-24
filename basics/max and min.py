lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input("Enter element"))
    lst.append(ele)
print(lst)
print("The Smallest Element in this List is : ", min(lst))
print("The Largest Element in this List is : ", max(lst))
print(type(lst))