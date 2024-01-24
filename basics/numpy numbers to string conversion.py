###Convert numbers =[1, 2.0, 3] to numpy array and convert all elements to string type

import numpy as np
numbers=np.array(1,2.0,3)

str = np.array_str(numbers)

print ("List: ", numbers)
print ("Strings: ", str)
print(type(str))