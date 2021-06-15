import pytest

from Data_Structures.quick_sort.quick_sort import QuickSort

def test_quick_sort():
    arr= [8,4,23,42,16,15]
    actual = QuickSort(arr, 0, len(arr)-1)
    expected = [4,8,15,16,23,42]
    assert actual == expected
