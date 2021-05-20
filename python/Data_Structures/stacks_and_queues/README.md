# Stacks and Queues
<!-- Short summary or background information -->
A stack is a collection that is based on the last-in-first-out (LIFO) policy.

A queue supports the insert and remove operations using a first-in first-out (FIFO) discipline.
## Challenge
<!-- Description of the challenge -->
Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.

Create a Stack class that has a top property. And add these methods:

`push`, `pop`, `peek`, `isEmpty`

Create a Queue class that has a front property. And add these methods:

`enqueue`, `dequeue`, `peek`, `isEmpty`

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
used the general known algorithms for stack methods and queue methods.

refer to this [article](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-10/resources/stacks_and_queues.html) to explore the algorithms used in the code.

BigO(1)
## API
<!-- Description of each method publicly available to your Stack and Queue-->

### Stack
- `push` which takes any value as an argument and adds a new node with that value to the top of the stack

- `pop` that does not take any argument, removes the node from the top of the stack

- `peek` that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack.

- `isEmpty` that takes no argument, and returns a boolean indicating whether or not the stack is empty

### Queue

- `enqueue` which takes any value as an argument and adds a new node with that value to the back of the queue.

- `dequeue` that does not take any argument, removes the node from the front of the queue, and returns the node’s value.

- `peek` that does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue.

- `isEmpty` that takes no argument, and returns a boolean indicating whether or not the queue is empty.
