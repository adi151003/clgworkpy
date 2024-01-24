import numpy as np

x = np.arange(5)  
print(x) 
y=x+10      
print(y)
z=x*3         
print(z)

mult1d=np.multiply(y,z)   
print(mult1d)



a = np.array([[1, 0],
              [0, 1]])
b = np.array([[4, 1],
              [2, 2]])
print(np.matmul(a, b))



a = np.arange(8).reshape((4,2))
b = np.arange(13,21).reshape((4,2))
##print(np.matmul(a, b))
print(a*b)    