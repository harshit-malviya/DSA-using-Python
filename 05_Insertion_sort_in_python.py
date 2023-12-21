def insertion_sort(list) :
    for i in range (1, len(list)):
        value = list[i]
        j = i-1
        while j>=0 and value<list[j]:
            list[j+1] = list[j]
            j-=1
        list[j+1] = value
    return list

list1 = [4, 2, 1, 5, 3]  
print("The unsorted list is:", list1)  
  
print("The sorted list1 is:", insertion_sort(list1)) 