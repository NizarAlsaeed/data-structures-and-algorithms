import pytest
from Data_Structures.stacks_and_queues.stacks_and_queues import Stack, Queue

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

def test_stack_peek(stack_instance,stack_testing_node):
    """Can successfully peek the next item on the stack"""
    actual = stack_instance.peek()
    expected = 'test'
    assert actual == expected


def test_stack_exception(stack_instance):
    """Calling pop or peek on empty stack raises exception"""
    with pytest.raises(Exception) as exc_info:
        actual = stack_instance.pop()
    actual = str(exc_info.value)
    expected = 'Cannot pop an empty Stack'
    assert actual == expected

    with pytest.raises(Exception) as exc_info:
        actual = stack_instance.peek()
    actual = str(exc_info.value)
    expected = 'Cannot peek an empty Stack'
    assert actual == expected



def test_queue_init():
    """Can successfully instantiate an empty queue"""
    queue = Queue()
    actual = queue.front
    expected = None
    assert actual == expected


def test_queue_enqueue(queue_instance):
    """    Can successfully enqueue into a queue
    Can successfully enqueue multiple values into a queue"""
    queue_instance.enqueue('test-one')
    queue_instance.enqueue('test-two')
    actual = queue_instance.__str__()
    expected = 'test-one | test-two | '
    assert actual == expected

def test_queue_dequeue(queue_instance, queue_2testing_nodes):
    """    Can successfully dequeue out of a queue the expected value
    Can successfully empty a queue after multiple dequeues"""
    queue_instance.dequeue()
    queue_instance.dequeue()
    actual = queue_instance.front
    expected = None
    assert actual == expected

def test_queue_peek(queue_instance, queue_testing_node):
    """Can successfully peek into a queue, seeing the expected value"""
    actual = queue_instance.peek()
    expected = 'test'
    assert actual == expected

def test_queue_exception(queue_instance):
    """Calling dequeue or peek on empty queue raises exception"""
    with pytest.raises(Exception) as exc_info:
        actual = queue_instance.dequeue()
    actual = str(exc_info.value)
    expected = 'Cannot dequeue an empty Queue'
    assert actual == expected

    with pytest.raises(Exception) as exc_info:
        actual = queue_instance.peek()
    actual = str(exc_info.value)
    expected = 'Cannot peek an empty Queue'
    assert actual == expected




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
