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
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        # 1. Create a list of size `max_size` with all values None
        self.hash_list = [None] * max_size

    # get the index value for a string
    def index_order(self, a_string, hash_list):
        order = 0
        for char in a_string:
            order += ord(char) # get the ascii value using ord()
        result = order % len(hash_list)  # get the reminder
        return result

    # handle linear probing
    def get_valid_index(self, key):
        # Start with the index returned by index_order
        idx = self.index_order(key,self.hash_list)
        
        while True:
            # Get the key-value pair stored at idx
            kv = self.hash_list[idx]
            
            # If it is None, return the index, this index is empty to store kv.
            if not kv:
                return idx
            
            # If the stored key matches the given key, return the index
            k, v = kv
            if k == key:
                return idx
            
            # Move to the next index
            idx += 1
            
            # Go back to the start if you have reached the end of the array
            if idx == len(self.hash_list):
                idx = 0
        
    def insert(self, key, value):
        """Insert a new key-value pair"""
        # 1. Find the index for the key using get_valid_index
        idx = self.get_valid_index(key)
        # 2. Store the key-value pair at the right index
        self.hash_list[idx] = (key, value)
    
    def find(self, key):
        """Find the value associated with a key"""
         # 1. Find the index for the key using index_order
        idx = self.index_order(key,self.hash_list)
        
        # 2. Retrieve the data stored at the index
        kv = self.hash_list[idx]
        
        # 3. Return the value if found, else return None
        if kv is None:
            return None
        else:
            key, value = kv
            return value
    
    def update(self, key, value):
        """Change the value associated with a key"""
         # 1. Find the index for the key using index_order
        idx = self.index_order(key,self.hash_list)
        self.hash_list[idx] = (key,value)
    
    def list_all(self):
        """List all the keys"""
        return [kv for kv in self.hash_list if kv is not None]



basic_table = HashTable()
print('len(basic_table.hash_list) == 4096?', len(basic_table.hash_list) == 4096)

basic_table = HashTable(max_size=1024)
print('len(basic_table.hash_list) == 1024?', len(basic_table.hash_list) == 1024)

# Insert some values
basic_table.insert('Aakash', '9999999999')
basic_table.insert('Hemanth', '8888888888')

# Find a value
print("basic_table.find('Hemanth') == '8888888888'? ", basic_table.find('Hemanth') == '8888888888')

# Update a value
basic_table.update('Aakash', '7777777777')
print("basic_table.find('Aakash') == '7777777777'? ", basic_table.find('Aakash') == '7777777777')

# Get the list of keys
print(basic_table.list_all() )

print("\n-----QUESTION 4: Handling Collisions with Linear Probing----------\n")

# New key 'listen' should return expected index
print("basic_table.get_valid_index('listen') == 655? ", basic_table.get_valid_index('listen') == 655)

basic_table.insert('listen', 99)

# Colliding key 'silent' should return next index
print("basic_table.get_valid_index('silent') == 656? ", basic_table.get_valid_index('silent') == 656)

print(basic_table.list_all())

print("\n------For Question 5, I have implimented the probing logic in the HashTable class----\n")


