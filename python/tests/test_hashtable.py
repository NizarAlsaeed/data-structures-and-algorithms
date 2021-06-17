import pytest
from Data_Structures.hashtable.hashtable import Hash_table

def test_hashtable():
    """Adding a key/value to your hashtable results in the value being in the data structure
    Retrieving based on a key returns the value stored
    Successfully returns null for a key that does not exist in the hashtable
    Successfully handle a collision within the hashtable
    Successfully retrieve a value from a bucket within the hashtable that has a collision
    Successfully hash a key to an in-range value"""
    hashtable = Hash_table()
    hashtable.add('test', 1)
    assert hashtable.contains('test')
    assert hashtable.get('test') == 1
    assert hashtable.get('unexistedkey') == None
    hashtable.add('tetr', 2) # creates a collision
    assert hashtable.contains('tetr')
    assert hashtable.get('tetr') == 2
    assert hashtable.hash('AnyKindOfKey')
