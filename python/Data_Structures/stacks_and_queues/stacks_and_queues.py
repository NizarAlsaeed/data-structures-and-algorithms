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
        if not self.is_empty():
            temp_node = self.top
            self.top = self.top.next
            temp_node.next = None
            return temp_node.value
        raise Exception("Cannot pop an empty Stack")

    def is_empty(self):
        """Returns True if Empty and false otherwise"""
        if self.top:
            return False
        return True

    def peek(self):
        """Returns the value at the top without modifying the stack, raises an exception otherwise"""
        if not self.is_empty():
            return self.top.value

        raise Exception("Cannot peek an empty Stack")

    def __str__(self):
        current = self.top
        output = ""
        while current:
            output += "\n" + str(current.value) + "\n-----------------"
            current = current.next
        return output


class Queue:
    def __init__(self):
        self.front = None

    def enqueue(self, value):
        """Add an item to the back of the queue"""
        node = Node(value)

        if not self.front:

            self.front = node
        else:
            current = self.front
            while current.next:
                current = current.next
            current.next = node
            node.next = None

    def dequeue(self):
        if not self.is_empty():
            temp_node = self.front
            self.front = self.front.next
            temp_node.next = None
            return temp_node.value
        raise Exception("Cannot dequeue an empty Queue")

    def is_empty(self):
        """Returns True if Empty and false otherwise"""
        if self.front:
            return False
        return True

    def peek(self):
        """Returns the value at the top without modifying the stack, raises an exception otherwise"""
        if not self.is_empty():
            return self.front.value

        raise Exception("Cannot peek an empty Queue")

    def __str__(self):
        current = self.front
        output = ""
        while current:
            output += str(current.value) + ' | '
            current = current.next
        return output

