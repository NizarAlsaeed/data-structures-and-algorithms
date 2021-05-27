# Trees
<!-- Short summary or background information -->
Trees are special data structur from graphs. In this challenge, we are using binary trees, for each node in these trees they have exactly two child-nodes untill the leaf node.

## Challenge
<!-- Description of the challenge -->
Define a method for each of the depth first traversals called preOrder, inOrder, and postOrder which returns an array of the values, ordered appropriately.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
for depth first traversals we applies recursive methods for the `preOrder`, `inOrder`, and, `postOrder`. and for the `add` method we also used recursive method to insert the new nodes to their proper place. And for the `contains` method we applied the iteratve method


BinarySearchTree:
- `contains`: space --> BigO(1) | time  --> BigO(height)
- `add`: space --> BigO(1) | time  --> BigO(n)
## API
<!-- Description of each method publicly available in each of your trees -->

 ```python

    # the same tree but the order of the returned node is different for each method
    preOrder(self):
        """depth first traversals"""
    preOrder(self):
        """depth first traversals"""
    preOrder(self):
        """depth first traversals"""

    add (self, value):
    """adds a new node with that value in the correct location in the binary search tree."""

    contains (self, value):
    """returns a boolean indicating whether or not the value is in the tree at least once."""


```
