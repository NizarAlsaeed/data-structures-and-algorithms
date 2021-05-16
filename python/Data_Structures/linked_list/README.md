# Challenge Summary
create and test a linked list data structure.
## Challenge Description
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
Within your LinkedList class, include a head property.
LinkedList must contain:
-   a method called insert which adds a new node
-   a method called includes which returns a boolean result - depending on whether that value exists as a Node’s value.
-   a method which returns a string representing all the values in the Linked List.

## Approach & Efficiency
-   Create Node class and assign it's properities
-   Create LinkedList class and assign it's properities
-   insert_method:
    - create node instance
    - point to the next node
    - assign next node to current pointer
    - assign new node to the next node
-   includes method:
    - start from head
    - compare value and return if true
    - next node
    - if current = null
    - return flase


BigO => Time O(N) | space O(1)

## API
<!-- Description of each method publicly available to your Linked List -->

**insert_method:**

insert into the linked list

**includes method:**

checks if a value is in the linked list

**__str__**

return a collection of all the values that exist in the linked list
