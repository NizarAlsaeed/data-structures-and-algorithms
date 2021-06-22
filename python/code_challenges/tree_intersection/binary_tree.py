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

    def breadth_first(self)->list:
        """ takes a Binary Tree as its unique input, traverse the input tree using a Breadth-first approach, and return a list of the values in the tree in the order they were encountered. """
        frontier = Queue()
        frontier.enqueue(self.root)
        explored = []
        current = None
        while not frontier.is_empty():
            current = frontier.dequeue()
            explored.append(current.value)
            if current.left:
                frontier.enqueue(current.left)
            if current.right:
                frontier.enqueue(current.right)
        return explored

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


