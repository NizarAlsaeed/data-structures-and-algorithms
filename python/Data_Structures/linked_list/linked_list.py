class Node:
  def __init__(self, value=None):
      self.value = value
      self.next = None
  def __str__(self):
    return self.value

class Linked_list:
  def __init__(self):
    self.head = None

  def insert (self, value=None):
    new_node = Node(value)
    if self.head :
        new_node.next = self.head
    self.head = new_node

  def append  (self, value):
    new_node = Node(value)
    if self.head :
      current = self.head
      while (current.next):
        current = current.next # point to the next node
      current.next = new_node
    else:
      self.head = new_node


  def insertBefore(self,value, new_val):
      new_node = Node(new_val)
      current = self.head
      if value == self.head.value:
          self.insert(new_val)
          return
      while(current):
        if current.next.value == value:
            new_node.next = current.next
            current.next = new_node
            break
        current = current.next

  def insertAfter(self,value,new_val):
      new_node = Node(new_val)
      current = self.head
      while(current):
        if current.value == value:
            new_node.next = current.next
            current.next = new_node
            break
        current = current.next

  def includes (self,value)->bool:
        if self.head :
            current = self.head
            while current:
                if current.value == value:
                    return True
                current = current.next
            return False
        else:
            return False


  def __str__(self):
    output = ""
    current = self.head
    while current:
      output +=  '{' + str(current.value) + '} -> '
      current = current.next
    output += 'None'

    return output

  def __repr__(self):
      return 'a linked_list instance'

