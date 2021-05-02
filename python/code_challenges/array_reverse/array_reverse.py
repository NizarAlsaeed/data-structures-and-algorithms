def reverseArray (ll):
    """Reverses a linked list
    Args:
        ll: linked list
    Returns:
        linked list in reversed form
    """
    ans=[]
    for element in ll:
        ans.insert(0,element)
    ll=ans
    return ll
