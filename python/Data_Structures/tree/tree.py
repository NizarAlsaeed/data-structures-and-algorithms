import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))
from stacks_and_queues.stacks_and_queues import Stack,Queue
#if you don't have it: https://github.com/NizarAlsaeed/data-structures-and-algorithms/blob/main/python/Data_Structures/stacks_and_queues/stacks_and_queues.py

class Node_BT:
    def __init__(self, value=None):
        """ properties for the value stored in the node, the left child node, and the right child node."""
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return self.value

class  BinaryTree:
    def __init__(self, root=None):
        self.root = root

    """the same tree but the order of the returned node is different for each method"""
    def preOrder(self)->list:
        """depth first traversals"""
        ans = []
        if self.root is not None:
            def _print(node):
                ans.append(node.value)
                if node.left:
                    _print(node.left)
                if node.right:
                    _print(node.right)

            _print(self.root)
            return ans
        else:
            raise Exception('The tree is empty')


    def inOrder(self)->list:
        """depth first traversals"""
        ans = []
        if self.root is not None:
            def _print(node):
                if node.left:
                    _print(node.left)

                ans.append(node.value)

                if node.right:
                    _print(node.right)

            _print(self.root)
            return ans
        else:
            raise Exception('The tree is empty')

    def postOrder(self)->list:
        """depth first traversals"""
        ans=[]
        if self.root is not None:
            def _print(node):
                if node.left:
                    _print(node.left)
                if node.right:
                    _print(node.right)
                ans.append(node.value)

            _print(self.root)
            return ans
        else:
            raise Exception('The tree is empty')

    def find_maximum_value(self):
        """ return the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric."""
        ans= float('-inf')
        if self.root is not None:
            def _max(node):
                nonlocal ans
                if node.value > ans:
                    ans = node.value
                if node.left:
                    _max(node.left)
                if node.right:
                    _max(node.right)

            _max(self.root)
            return ans
        else:
            raise Exception('The tree is empty')

    def __str__(self):
        """the default is to print the preOrder list"""
        return self.preOrder()



class BinarySearchTree(BinaryTree):

    def __init__(self, root=None):
        super().__init__(root=root)

    def add (self, value):
        """adds a new node with that value in the correct location in the binary search tree."""

        new_node_BT = Node_BT(value)

        def traverse_and_add(root):
            if root.value >= value:
                if not root.left:
                    #print(f'L of {root.value}')
                    setattr(root, 'left', new_node_BT)
                else:
                    traverse_and_add(root.left)
            else:
                if not root.right:
                    #print(f'R of {root.value}')
                    setattr(root, 'right', new_node_BT)
                else:
                    traverse_and_add(root.right)

        traverse_and_add(self.root)


    def contains (self, value):
        """returns a boolean indicating whether or not the value is in the tree at least once."""
        root = self.root
        while root:
            if root.value == value:
                return True
            elif root.value > value:
                if root.left:
                    root = root.left
                else: return False

            else:
                if root.right:
                    root = root.right
                else: return False
        return False


if __name__=='__main__':
    abs_root = Node_BT(2)

    abs_root.left = Node_BT(7)
    abs_root.right = Node_BT(5)

    abs_root.left.left = Node_BT(2)
    abs_root.left.right = Node_BT(6)

    abs_root.right.right = Node_BT(9)
    binary_tree = BinaryTree(abs_root)
    print(binary_tree.find_maximum_value())
    print('------------------------------------')
    binary_tree.preOrder()
    print('--pre')
    binary_tree.inOrder()
    print('--in')
    binary_tree.postOrder()
    print('--post')

    binary_search_tree = BinarySearchTree(Node_BT(23))
    binary_search_tree.add(15)
    binary_search_tree.add(4)
    binary_search_tree.add(90)

    binary_search_tree.preOrder()
    print(binary_search_tree.contains(15))
