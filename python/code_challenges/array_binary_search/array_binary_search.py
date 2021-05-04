import math

def BinarySearch(input_list:list, search_key)->int:
    """
    return the index of the array’s element that is equal to the search key,
    or
    return -1 if the element does not exist.
    """
    sorted_list = sort_list(input_list)
    while len(sorted_list) >=1:
        middle_index = math.ceil(len(sorted_list)/2)
        if search_key == sorted_list[middle_index]:
            return middle_index
        elif search_key > sorted_list[middle_index]:
            sorted_list = sorted_list[middle_index+1:]
            continue
        else:
            sorted_list = sorted_list[:middle_index]
    if sorted_list and (sorted_list[0] == search_key):
        return sorted_list[0]
    else:
        return -1

def sort_list(input_list:list)->list:
    holder = 0
    sorted = False

    while not sorted :
        sorted = True
        for i in range(len(input_list)-1):
            if input_list[i+1] - input_list [i] < 0:
                sorted = False
                holder=input_list[i]
                input_list[i]=input_list[i+1]
                input_list[i+1]=holder
    return input_list
