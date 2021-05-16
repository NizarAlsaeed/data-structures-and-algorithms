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


def test_append(an_instance):
    """
    Can successfully add a node to the end of the linked list
    """
    an_instance.append('test')
    actual = an_instance.includes('test')
    expected = True
    assert actual == expected

def test_multiple_append(an_instance):
    """
    Can successfully add multiple nodes to the end of a linked list
    """
    an_instance.append('test_one')
    an_instance.append('test_two')
    actual = an_instance.includes('test_one') and an_instance.includes('test_two')
    expected = True
    assert actual == expected

def test_insert_before(an_instance,add_2testing_nodes):
    """
    Can successfully insert a node before a node located i the middle of a linked list
    """
    an_instance.insertBefore('test-two','new-test')
    actual = an_instance.__str__()
    expected = '{test-one} -> {new-test} -> {test-two} -> None'
    assert actual == expected

def test_insert_before_first_node(an_instance,add_2testing_nodes):
    """
    Can successfully insert a node before the first node of a linked list
    """
    an_instance.insertBefore('test-one','new-test')
    actual = an_instance.__str__()
    expected = '{new-test} -> {test-one} -> {test-two} -> None'
    assert actual == expected


def test_insert_after(an_instance,add_2testing_nodes):
    """
    Can successfully insert after a node in the middle of the linked list
    """
    an_instance.insertAfter('test-one','new-test')
    actual = an_instance.__str__()
    expected = '{test-one} -> {new-test} -> {test-two} -> None'
    assert actual == expected

def test_insert_after_last_node(an_instance,add_2testing_nodes):
    """
    Can successfully insert a node after the last node of the linked list
    """
    an_instance.insertAfter('test-two','new-test')
    actual = an_instance.__str__()
    expected = '{test-one} -> {test-two} -> {new-test} -> None'
    assert actual == expected



@pytest.fixture
def an_instance():
    return Linked_list()

@pytest.fixture
def add_testing_node(an_instance):
    an_instance.insert('test')

@pytest.fixture
def add_2testing_nodes(an_instance):
    an_instance.insert('test-two')
    an_instance.insert('test-one')
