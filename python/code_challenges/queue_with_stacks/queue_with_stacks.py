class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value


class Stack:
    def __init__(self, node=None):
        self.top = node

    def push(self, value):
        if not self.top:
            self.top = Node(value)
        else:
            node = Node(value)
            node.next = self.top
            self.top = node

    def pop(self):
        if self.top:
            temp_node = self.top
            self.top = self.top.next
            temp_node.next = None
            return temp_node.value
        raise Exception("Cannot pop an empty Stack")

    def peek(self):
        """Returns the value at the top without modifying the stack, raises an exception otherwise"""
        if not self.is_empty():
            return self.top.value

        raise Exception("Cannot peek an empty Stack")


class PseudoQueue:
    def enqueue(self,value):
        """ inserts value into the PseudoQueue, using a first-in, first-out approach."""
        pass
    def dequeue(self):
        """ extracts a value from the PseudoQueue, using a first-in, first-out approach."""
        pass
