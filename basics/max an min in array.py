arr = []
n = int(input("Enter size of array : "))
for x in range(n):
    x=int(input("Enter element of array : "))
    arr.append(x)
largest = arr[0]
smallest = arr[0]
for i in range(n):
    if arr[i]>largest:
        largest = arr[i]
    if arr[i]<smallest:
        smallest = arr[i]

print("Array is : ",arr)      
print("Largest element in array is :",largest)
print("Smallest element in array is :",smallest) 