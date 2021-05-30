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


@pytest.fixture
def ex_instance():
    binary_tree = BinarySearchTree(Node_BT(2))
    binary_tree.add(1)
    binary_tree.add(3)
    return binary_tree
