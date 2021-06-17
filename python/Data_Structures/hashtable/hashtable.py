import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))
from linked_list.linked_list import Linked_list

class Hash_table:
    def __init__(self, length=1024):
        self.table = [Linked_list()] * length

    def hash(self, key: str) -> int:
        """takes in an arbitrary key and returns an index in the collection."""
        asci = 0
        for char in key:
            asci += ord(char)
        index = asci * 599 % 1024
        return index

    def add(self, key, value):
        """takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed."""
        index = self.hash(key)
        comb = (key, value)
        self.table[index].insert(comb)

    def get(self, key):
        """takes in the key and returns the value from the table."""
        index = self.hash(key)
        linked_list = self.table[index]
        if linked_list.head:
            current = linked_list.head
            while current:
                if current.value[0] == key:
                    return current.value[1]
                current = current.next
        raise ValueError('Key not found')

    def contains(self, key) -> bool:
        """takes in the key and returns a boolean, indicating if the key exists in the table already."""
        try:
            self.get(key)
        except:
            return False
        else:
            return True


if __name__ == '__main__':
    hash_table = Hash_table()
    hash_table.add('nizar', 25)
    hash_table.add('Ahmed', 19)

    print(hash_table.get('Ahmed'))
