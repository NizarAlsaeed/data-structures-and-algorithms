
def insertShiftArray (input_list: list, v) -> list:
    """
    takes in a list and the value to be added.
    return a list with the new value added at the middle index.
    """
    input_list_length = len(input_list)
    middle_index = input_list_length//2
    ans=[0]*(input_list_length+1)

    if input_list_length %2:
        middle_index+=1

    for index in range(len(ans)):
        if index < middle_index:
            ans[index]=input_list[index]

        elif index == middle_index:
            ans[index]=v

        elif index > middle_index:
            ans[index]=input_list[index-1]
    return ans
