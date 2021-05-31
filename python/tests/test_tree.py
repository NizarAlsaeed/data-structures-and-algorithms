import pytest
from Data_Structures.tree.tree import Node_BT ,BinaryTree, BinarySearchTree


def test_empty_tree():
    """    Can successfully instantiate an empty tree"""
    binary_tree = BinaryTree()
    actual = binary_tree.root
    expected = None
    assert actual == expected

def test_single_node_tree():
    """    Can successfully instantiate a tree with a single root node"""
    binary_tree = BinaryTree(Node_BT('True'))
    actual = binary_tree.root.value
    expected = 'True'
    assert actual == expected

def test_add():
    """    Can successfully add a left child and right child to a single root node"""
    binary_tree = BinarySearchTree(Node_BT(2))
    binary_tree.add(1)
    binary_tree.add(3)
    actual = binary_tree.preOrder()
    expected = [2,1,3]
    assert actual == expected


def test_order():
    """    Can successfully return a collection from a preorder traversal
    Can successfully return a collection from an inorder traversal
    Can successfully return a collection from a postorder traversal
"""
    binary_tree = BinarySearchTree(Node_BT(2))
    binary_tree.add(1)
    binary_tree.add(3)
    actual = [binary_tree.preOrder(), binary_tree.inOrder(), binary_tree.postOrder()]
    expected = [[2,1,3], [1,2,3], [1,3,2]]
    assert actual == expected


def test_max_value(ex_instance):
    """    Can successfully return the max value in a tree"""
    actual = ex_instance.find_maximum_value()
    expected = 3
    assert actual == expected


def test_breadth_first(breadth_instance):
    """    Can successfully return the traversed list of breadth first"""
    actual = breadth_instance.breadth_first()
    expected = [2, 7, 5, 2, 6, 9, 5, 11, 4]
    assert actual == expected

@pytest.fixture
def ex_instance():
    binary_tree = BinarySearchTree(Node_BT(2))
    binary_tree.add(1)
    binary_tree.add(3)
    return binary_tree

@pytest.fixture
def breadth_instance():
    abs_root = Node_BT(2)

    abs_root.left = Node_BT(7)
    abs_root.right = Node_BT(5)

    abs_root.left.left = Node_BT(2)
    abs_root.left.right = Node_BT(6)

    abs_root.right.right = Node_BT(9)

    abs_root.left.right.left = Node_BT(5)
    abs_root.left.right.right = Node_BT(11)

    abs_root.right.right.right = Node_BT(4)

    binary_tree = BinaryTree(abs_root)
    return binary_tree
