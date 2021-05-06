import pytest
from Data_Structures.linked_list.linked_list import Linked_list, Node

def test_instantiattion(an_instance):
    """
    test if it Can successfully instantiate an empty linked list
    """
    actual = an_instance.head
    expected = None
    assert actual == expected

def test_insert(an_instance):
    """
    if it can properly insert into the linked list
    and
    if it Will return true when finding a value within the linked list that exists
    """
    an_instance.insert('test')
    actual = an_instance.includes('test')
    expected = True
    assert actual == expected

def test_head(an_instance,add_testing_node):
    """
    if The head property will properly point to the first node in the linked list
    """
    actual = an_instance.head.value
    expected = 'test'
    assert actual == expected

def test_multiple_nodes(an_instance,add_2testing_nodes):
    """
    if it can Can properly insert multiple nodes into the linked list
    """
    actual = an_instance.includes('test-one') and an_instance.includes('test-two')
    expected = True
    assert actual == expected


def test_No_value(an_instance):
    """
    Will return false when searching for a value in the linked list that does not exist
    """
    actual = an_instance.includes('test')
    expected = False
    assert actual == expected


def test_all_values(an_instance,add_2testing_nodes):
    """
    can properly return a collection of all the values that exist in the linked list
    """
    actual = an_instance.__str__()
    expected = '{test-one} -> {test-two} -> None'
    assert actual == expected



@pytest.fixture
def an_instance():
    return Linked_list()

@pytest.fixture
def add_testing_node(an_instance):
    an_instance.insert('test')

@pytest.fixture
def add_2testing_nodes(an_instance):
    an_instance.insert('test-one')
    an_instance.insert('test-two')
