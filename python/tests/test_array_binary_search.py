from code_challenges.array_binary_search.array_binary_search import BinarySearch


def test_BinarySearch_one():

    actual = BinarySearch([4,8,15,16,23,42], 15)
    expected = 2
    assert actual == expected, 'must return the index of the array’s element that is equal to the search key'


def test_BinarySearch_two():

    actual = BinarySearch([11,22,33,44,55,66,77], 90)
    expected = -1
    assert actual == expected, 'must return  -1 if the element does not exist'


def test_BinarySearch_three():

    actual = BinarySearch([1, 2, 3, 5, 6, 7], 4)
    expected = -1
    assert actual == expected, 'must return  -1 if the element does not exist'
