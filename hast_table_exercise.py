"""
Dictionaries in Python are implemented using a data structure called hash table. 
A hash table uses a list/array to store the key-value pairs, and uses a hashing 
function to determine the index for storing or retrieving the data associated 
with a given key.
"""

# As a first step is to create a Python list which will hold all the key-value pairs. 
# We'll start by creating a list of a fixed size.

print('\n--QUESTION 1: Create a Python list of size `MAX_HASH_TABLE_SIZE`, \
    with all the values set to `None`.--\n')

# global variable
MAX_HASH_TABLE_SIZE = 4096

hash_list = [None] * MAX_HASH_TABLE_SIZE

print('len(hash_list) == MAX_HASH_TABLE_SIZE: ',len(hash_list) == MAX_HASH_TABLE_SIZE)

print('\n---------------QUESTION 2: Impliment Hashing Function------------------\n')

"""
Algorithm for hashing, which can convert strings into numeric list indices.

1. Iterate over the string, character by character
2. Convert each character to a number using Python's built-in ord function.
3. Add the numbers for each character to obtain the hash for the entire string
4. Take the remainder of the result with the size of the data list
"""
def index_order(a_string, hash_list):
    order = 0
    for char in a_string:
        order += ord(char) # get the ascii value using ord()
    result = order % len(hash_list)  # get the reminder
    return result

print(index_order("Pranay", hash_list))

print('\n-------Insert-------\n')

key, value = "Pranay", 7030026662
idx = index_order(key,hash_list)
#one way
hash_list[idx] = (key, value)

# another
hash_list[index_order('Hemanth', hash_list)] = ('Hemanth', '9595949494')

print('\n-------Find-------\n')
idx = index_order('Hemanth', hash_list)
idx
key, value = hash_list[idx]
print(key, value)

print('\n-------List-------\n')
# print(list(filter(lambda x: x is not None, hash_list)))
pairs = [kv for kv in hash_list if kv is not None]
print(pairs)    


print("\n-----------QUESTION3: Creat a Class to implement the hashing algorithm.-------------\n")

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


