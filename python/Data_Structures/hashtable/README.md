# Hashtables
<!-- Short summary or background information -->
A hash is the result of some algorithm taking an incoming string and converting it into a value that could be used for either security or some other purpose. In the case of a hashtable, it is used to determine the index of the array.
## Challenge
<!-- Description of the challenge -->
Implement a Hashtable with the following methods: add, get, contains, hash.
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- initialized a table with an array of linked list to handle collisions
- created the hash method based on the ASCI values of the key
- used linkedlist insert method to add the key and value as a tuble
- traversed on the linkedlist and checked for the key for the get method

BigO(1)
## API
<!-- Description of each method publicly available in each of your hashtable -->
`add`: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

`get`: takes in the key and returns the value from the table.

`contains`: takes in the key and returns a boolean, indicating if the key exists in the table already.

`hash`: takes in an arbitrary key and returns an index in the collection.
