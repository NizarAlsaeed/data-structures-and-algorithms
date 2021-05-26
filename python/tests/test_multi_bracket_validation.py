import pytest
from code_challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_balanced_brackets():
    ans = []
    tl = ['{}' ,'{}(){}', '[[()]]','()[[Extra Characters]]', '(){}[[]]', '{}{Code}[Fellows](())']
    for st in tl:
        ans.append(multi_bracket_validation(st))
    actual = ans
    expected = [True]*6
    assert actual == expected

def test_unbalanced_brackets():
    ans = []
    fl =['[({}]', '(](', '{(})']
    for st in fl:
        ans.append(multi_bracket_validation(st))
    actual = ans
    expected = [False]*3
    assert actual == expected
