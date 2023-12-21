# bubble sort program
l1 = [2,93,1,6,3,67,31,8,34]

def bubble_sort(list) :
    for i in range(0 , len(list) -1 ):
        for j in range(0 , len(list) - 1):
            if list[j] > list[j+1] :
                temp = list[j+1]
                list[j+1] = list[j]
                list[j] = temp
    return list

print("Unsorted List = ",l1)
l2 = bubble_sort(l1)
print("Sorted List = ",l2)