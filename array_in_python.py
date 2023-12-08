from array import *
# there is no native array in python, "array" is a external module of python, we use NUMPY to use array in python
# the array in python are dynamic in nature 
a1 = array("i" , [23,55,12,121] )
print(a1[2])
# increasing the size of array during runtime
a1.append(41)
print(a1)
