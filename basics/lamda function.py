def sortarray(array):
      
    for i in range(len(array[0])):
        sortedcolumn = sorted(array, key = lambda x:x[i])
        
        print("Sorted array specific to column {}, \
        {}".format(i, sortedcolumn))

array = [['java', 1995], ['c++', 1983],['python', 1989]]
sortarray(array)