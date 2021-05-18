from Data_Structures.linked_list.linked_list import Linked_list

def zipLists(ll_one,ll_two):
    """
    takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list. Try and keep additional space down to O(1).
    """
    ll = Linked_list()
    current1 = ll_one.head
    current2 = ll_two.head
    if ll_one.length() > ll_two.length():
        longer_ll = ll_one.length()
    else:
        longer_ll = ll_two.length()

    for i in range(longer_ll):
        if current1:
            ll.append(current1.value)
            current1 = current1.next
        if current2:
            ll.append(current2.value)
            current2 = current2.next

    return ll.__str__()
