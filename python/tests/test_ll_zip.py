import pytest
from Data_Structures.linked_list.linked_list import Linked_list
from code_challenges.ll_zip.ll_zip import zipLists

def test_zipLists():

    ll1 = Linked_list()
    for i in range(1,5):
        ll1.append(i)

    ll2 = Linked_list()
    for i in range(5,10):
        ll2.append(i)

    actual = zipLists(ll1,ll2)

    expected = '{1} -> {5} -> {2} -> {6} -> {3} -> {7} -> {4} -> {8} -> {9} -> None'
    assert actual == expected


