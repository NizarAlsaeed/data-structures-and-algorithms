
def hmap_join(hmap1, hmap2, type='left'):
    """LEFT JOINs two hashmaps into a single data structure
    The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
    The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
    """
    if type.lower() == 'right':
        temp = hmap1
        hmap1 = hmap2
        hmap2 = temp
    elif type.lower() != 'left':
        raise ValueError('type argument must be either left or right')

    joined = [None]*len(hmap1)
    second_value = None
    for i,key in enumerate(hmap1):
        if hmap2.get(key):
            second_value = hmap2.get(key)
        else:
            second_value = None
        joined[i] = (key, hmap1.get(key), second_value)
    
    return joined
        

if __name__=='__main__':
    dict1 = {
        'fond':'enamored',
        'wrath':'anger',
        'diligent':'employed',
        'outfit':'grab',
        'guide':'usher',
    }

    dict2 = {
        'fond':'averse',
        'wrath':'delight',
        'diligent':'idle',
        'guide':'follow',
        'flow':'jam'
    }

    print(hmap_join(hmap1=dict1, hmap2=dict2, type='left'))