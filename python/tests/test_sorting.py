import pytest
from Data_Structures.sorting.sorting import insertion_sort

def test_insertion_sort():
    actual = insertion_sort([8, 4, 2, 3, 4, 2, 16, 15])
    expected = [2, 2, 3, 4, 4, 8, 15, 16]
    assert actual == expected
