# Challenge Summary
<!-- Description of the challenge -->
*Find common values in 2 binary trees.*

takes two binary tree parameters.

Without utilizing any of the built-in library methods available to your language,
return a set of values found in both trees.
## Whiteboard Process
<!-- Embedded whiteboard image -->

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- traverse in both trees using preOrder
- looping through the second list representing the second binary tree
- checkng if value is not in the first list
- replace the value with empty string 
- return the seond list

## Solution
<!-- Show how to run your code, and examples of it in action -->

```python
# create two binary trees
    # first binary tree
    bt1 = BinaryTree(Node_BT(150))

    bt1.root.left = Node_BT(100)
    bt1.root.right = Node_BT(250)

    bt1.root.left.left = Node_BT(75)
    bt1.root.left.right = Node_BT(160)

    bt1.root.right.right = Node_BT(350)
    bt1.root.right.left = Node_BT(200)

    bt1.root.left.right.left = Node_BT(125)
    bt1.root.left.right.right = Node_BT(175)

    bt1.root.right.right.left = Node_BT(300)
    bt1.root.right.right.right = Node_BT(500)

    # second binary tree
    bt2 = BinaryTree(Node_BT(42))
    
    bt2.root.left = Node_BT(100)
    bt2.root.right = Node_BT(600)

    bt2.root.left.left = Node_BT(15)
    bt2.root.left.right = Node_BT(160)

    bt2.root.right.right = Node_BT(350)
    bt2.root.right.left = Node_BT(200)

    bt2.root.left.right.left = Node_BT(125)
    bt2.root.left.right.right = Node_BT(175)

    bt2.root.right.right.left = Node_BT(4)
    bt2.root.right.right.right = Node_BT(500)

    print(bt1.preOrder(),bt2.preOrder())
    # assign the trees into the function
    print(tree_intersection(bt1,bt2))

>> ['', 100, '', 160, 125, 175, '', 200, 350, '', 500]
```