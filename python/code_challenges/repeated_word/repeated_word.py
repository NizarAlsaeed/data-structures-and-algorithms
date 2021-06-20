import  re

class Node:
  def __init__(self, value=None):
      self.value = value
      self.next = None
  def __str__(self):
    return self.value

class Linked_list:
  def __init__(self):
    self.head = None

  def append  (self, value):
    new_node = Node(value)
    if self.head :
      current = self.head
      while (current.next):
        current = current.next # point to the next node
      current.next = new_node
    else:
      self.head = new_node

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

def main(sentence:str)->str:
    """return the first word to occur more than once in that provided string"""
    words_list = re.findall(r'\w+', sentence)
    ll = Linked_list()
    for word in words_list:
        if ll.includes(word):
            return word
        ll.append(word.lower())

if __name__ == '__main__':
    print(main("Once upon a time, there was a brave princess who..."))
    print(main("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."))
    print(main("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."))
