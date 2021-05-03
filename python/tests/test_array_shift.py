from code_challenges.array_shift.array_shift import  insertShiftArray


def test_insertShiftArray_one():

    actual = insertShiftArray([2,4,6,8], 5)
    expected = [2,4,5,6,8]
    assert actual == expected, 'value should be added to the middle of the list'


def test_insertShiftArray_two():

    actual = insertShiftArray([4,8,15,23,42], 16)
    expected = [4,8,15,16,23,42]
    assert actual == expected, 'value should be added to the middle of the list'
