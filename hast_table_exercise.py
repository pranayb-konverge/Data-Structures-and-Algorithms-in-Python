"""
Dictionaries in Python are implemented using a data structure called hash table. 
A hash table uses a list/array to store the key-value pairs, and uses a hashing 
function to determine the index for storing or retrieving the data associated 
with a given key.
"""

print("\n-----------Creat a Class to implement the hashing algorithm.-------------\n")

"""
Your objective in this assignment is to implement a HashTable class which supports 
the following operations:

Insert: Insert a new key-value pair
Find: Find the value associated with a key
Update: Update the value associated with a key
List: List all the keys stored in the hash table

"""

class HashTable:

    def insert(self, key, value):
        """Insert a new key-value pair"""
        pass
    
    def find(self, key):
        """Find the value associated with a key"""
        pass
    
    def update(self, key, value):
        """Change the value associated with a key"""
        pass
    
    def list_all(self):
        """List all the keys"""
        pass

# As a first step is to create a Python list which will hold all the key-value pairs. 
# We'll start by creating a list of a fixed size.

# global variable
MAX_HASH_TABLE_SIZE = 4096

print('\n--QUESTION 1: Create a Python list of size `MAX_HASH_TABLE_SIZE`, \
    with all the values set to `None`.--\n')

hash_list = [None] * MAX_HASH_TABLE_SIZE

print('len(hash_list) == MAX_HASH_TABLE_SIZE: ',len(hash_list) == MAX_HASH_TABLE_SIZE)