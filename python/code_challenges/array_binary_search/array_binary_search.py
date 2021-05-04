import math

def BinarySearch(input_list:list, search_key)->int:
    """
    return the index of the array’s element that is equal to the search key,
    or
    return -1 if the element does not exist.
    """
    sorted_list = sort_list(input_list)
    while len(sorted_list) !=1:
        middle_index = math.ceil(len(input_list)/2)
        if search_key == list[middle_index]:
            return middle_index
        elif search_key > list[middle_index]:
            sorted_list = list[middle_index+1:]
            continue
        else:
            sorted_list = list[:middle_index-1]

def sort_list(input_list):
    holder = 0
    for i in range(len(input_list)):
        if i == 0:
            continue
        if input_list[i] - input_list [i-1] < 0:
            holder=input_list[i-1]
            input_list[i-1]=input_list[i]
            input_list[i]=holder
    return input_list


print(sort_list([1,5,3,4,2]))
