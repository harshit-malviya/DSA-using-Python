from array import *
# there is no native array in python, "array" is a external module of python, we use NUMPY to use array in python

#list is define in "bulitin" module
#array is define in "array" module

# Difference btw array and list is in array we can only store homogeneous type of data but in list we can store hetrogeneous type of data

# the array in python are dynamic in nature
 
# array = array("typecode",[elements])
# i = signed int

a1 = array("i" , [23,55,12,121] )
print(a1[2])
# increasing the size of array during runtime
print(a1)
a1.append(41)
print(a1)
for x in a1:
    print(x)

# Difference between Signed Int and Unsigned Int 

""" Signed Int	

 1. A signed int can store both positive and negative values.	
 2. A signed integer can hold values from
   -2³²/2 - 1 (-2147483648) to 2³²/2 - 1 ( 2147483647 )	
 3. A signed integer can get an overflow error while used in a program with larger values.	"""


"""  Unsigned Int

 1. Unsigned integer values can only store non-negative values.
 2. A 32-bit unsigned integer can store only positive values from 0 to 2^32 -1 ( 4294967295 )
 3. Wraps around to 0 if the value exceeds the maximum limit. """