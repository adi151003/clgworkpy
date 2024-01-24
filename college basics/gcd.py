def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)
  
a = int(input ("Enter a value"))
b = int(input ("Enter a value"))
  

print("The gcd of ",a, "and ", b, "is : " ,gcd(a,b))
