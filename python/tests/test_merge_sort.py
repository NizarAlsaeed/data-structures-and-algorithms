import pytest

from Data_Structures.merge_sort.merge_sort import mergesort


def test_merge_sort():
    actual = mergesort([8,4,23,42,16,15])
    expected = [4,8,15,16,23,42]
    assert actual == expected

    
