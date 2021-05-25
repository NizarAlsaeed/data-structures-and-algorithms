import pytest
from code_challenges.fifo_animal_shelter.fifo_animal_shelter import AnimalShelter,Cat,Dog

def test_enqueue(instances:list):

    for i in range(1,4):
        instances[0].enqueue(instances[i])
    actual = instances[0].__str__()
    expected = 'ketty, rex, jack'
    assert actual == expected

def test_dequeue(instances):
    for i in range(1,4):
        instances[0].enqueue(instances[i])
    instances[0].dequeue('dog')
    actual = instances[0].__str__()
    expected = 'ketty, jack'
    assert actual == expected

def test_dequeue_none(instances):
    actual = instances[0].dequeue('do7')
    expected = None
    assert actual == expected

@pytest.fixture
def instances():
    animal_shelter = AnimalShelter()
    ketty = Cat('ketty', 1)
    rex = Dog('rex',2)
    jack = Dog('jack', 3)
    return [animal_shelter, ketty, rex, jack]
