lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
count = 0
  
for i in lst:
    count += i

avg = count/len(lst)
print("sum = ", count)
print("average = ", avg)