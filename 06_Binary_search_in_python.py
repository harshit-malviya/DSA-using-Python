
# def binary_search(list,data):
#     start = 0
#     last = len(list)-1
#     mid = 0
#     while start <= last:
#         mid = (start + last)//2
#         if list[mid] < data :
#             start = mid+1
#         elif list[mid] < data:
#             last = mid-1
#         else:
#             return mid
#     return -1

# l1 = [2,4,8,34,53,66,68,87,99,224]
# x = 66
# s = binary_search(l1,x)
# if s==-1:
#     print("Element is not in list")
# else:
#     print(f"Element {x} found in List")

# Binary Search in python

# # https://www.programiz.com/dsa/binary-search
def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")

