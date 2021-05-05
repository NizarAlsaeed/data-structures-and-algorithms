import math

def BinarySearch(input_list:list, search_key)->int:
    """
    return the index of the array’s element that is equal to the search key,
    or
    return -1 if the element does not exist.
    """
    input_list = sort_list(input_list)

    first_index = 0
    last_index = len(input_list)-1
    while first_index != last_index:
        middle = math.ceil((first_index + last_index) / 2)
        if input_list[middle] > search_key:
            last_index = middle - 1
        else:
            first_index = middle
    if input_list[first_index] == search_key:
        return first_index
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
