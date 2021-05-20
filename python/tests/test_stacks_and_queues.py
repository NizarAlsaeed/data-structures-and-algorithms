import pytest
from Data_Structures.stacks_and_queues.stacks_and_queues import Stack, Queue
"""

    Calling pop or peek on empty stack raises exception

    Calling dequeue or peek on empty queue raises exception

"""
def test_stack_init():
    """Can successfully instantiate an empty stack"""
    stack = Stack()
    actual = stack.top
    expected = None
    assert actual == expected

def test_stack_push(stack_instance):
    """ Can successfully push onto a stack
        Can successfully push multiple values onto a stack"""
    stack_instance.push('test-one')
    stack_instance.push('test-two')
    actual = stack_instance.__str__()
    expected = """
test-two
-----------------
test-one
-----------------"""
    assert actual == expected

def test_stack_pop(stack_instance,stack_2testing_nodes):
    """ Can successfully pop off the stack
        Can successfully empty a stack after multiple pops"""
    stack_instance.pop()
    stack_instance.pop()
    actual = stack_instance.top
    expected = None
    assert actual == expected

def test_stack_peek():
    """Can successfully peek the next item on the stack"""
    pass


def test_queue_init():
    """Can successfully instantiate an empty queue"""
    queue = Queue()
    actual = queue.front
    expected = None
    assert actual == expected



def test_queue_enqueue():
    """    Can successfully enqueue into a queue
    Can successfully enqueue multiple values into a queue"""
    pass

def test_queue_dequeue():
    """    Can successfully dequeue out of a queue the expected value
    Can successfully empty a queue after multiple dequeues"""
    pass

def test_queue_peek():
    """Can successfully peek into a queue, seeing the expected value"""
    pass








@pytest.fixture
def stack_instance():
    return Stack()

@pytest.fixture
def queue_instance():
    return Queue()

@pytest.fixture
def stack_testing_node(stack_instance):
    stack_instance.push('test')

@pytest.fixture
def stack_2testing_nodes(stack_instance):
    stack_instance.push('test-one')
    stack_instance.push('test-two')

@pytest.fixture
def queue_testing_node(queue_instance):
    queue_instance.enqueue('test')

@pytest.fixture
def queue_2testing_nodes(queue_instance):
    queue_instance.enqueue('test-one')
    queue_instance.enqueue('test-two')
