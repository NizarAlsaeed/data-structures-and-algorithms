import pytest
from code_challenges.left_join.left_join import hmap_join


def test_hmap_join():
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

    actual = hmap_join(hmap1=dict1, hmap2=dict2, type='left')
    expected = [
                    ('fond', 'enamored', 'averse'),
                    ('wrath', 'anger', 'delight'),
                    ('diligent', 'employed', 'idle'),
                    ('outfit', 'grab', None),
                    ('guide', 'usher', 'follow')
                ]

    assert actual == expected

