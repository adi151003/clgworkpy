def numbers(n1, n2):
    results = []
    for i in range(n1, n2+1):
        if (i%7==0) and (i%5!=0):
            results.append(i)
    return results
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
print(numbers(n1,n2))