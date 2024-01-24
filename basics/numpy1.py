import numpy as np

t= np.array ([61, 22, 32, 45])  ##gives output in true false
print(t<35)

x = np.arange(5)  ## to make a 1d matrix of elements 0 to 4
print(x) 
y=x+10        ### add 10 in all elements
print(y)



z=x*3            ##multiply 3 in all elements
print(z)

mult1d=np.multiply(y,z)   ##multiply 2 1d matrix
print(mult1d)

n = np.arange(8,16,1).reshape((2,4))   ###make a 2d matrix starting from 8 to 15 with a gap of 1 with 2 rows and 4 coloumns 
print(n)  
print('1st element on 2nd row: \n ', n[1, 2]) ### find element using index
print(n.sum(axis=0) ) ##sum of each coloummn
print(n.min(axis=1)) ###min of each row
print(n.transpose()) ## transpose of a matrix



arr = np.arange(24).reshape((4,3,2))    ###make a 3d matrix starting with 24 elemnts with 4 layers in 3d , 3 rows and 2 coloumns
print(arr)
print(arr[2, 2, 1])   ### find element using index


array = np.array([1, 2, 3, 4]) 
print(array)
print(array[2] + array[3])   ## add elements at the given indexes


r = np.random.normal(size=15)
print(r)