"""

QUESTION 1: As a senior backend engineer at Jovian, you are tasked with developing a 
fast in-memory data structure to manage profile information (username, name and email) 
for 100 million users. It should allow the following operations to be performed efficiently:

1. Insert the profile information for a new user.
2. Find the profile information of a user, given their username
3. Update the profile information of a user, given their usrname
4. List all the users of the platform, sorted by username
You can assume that usernames are unique.

"""

print("\n-----------Question 1:  Write a function to insert \
    a new node into a BST.--------------\n")

# create the user class
class User:
    # in the constructor assing the variables
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        
    # Use this magic function to create the representation of the class data
    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)
    
    # To print the User data we can use this magic function
    def __str__(self):
        return self.__repr__()


# Add some data to the User object and save in the users list
aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

# This classs will help in the CRUD opration on this in memory db
class UserDatabase:
    def __init__(self):
        self.users = []
    
    def insert(self, user):
        i = 0
        while i < len(self.users):
            # Find the first username greater than the new user's username
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)
    
    def find(self, username):
        for user in self.users:
            # Find the username 
            if user.username == username:
                return user
    
    def update(self, user):
        # Use the inbuild function to find the user and update the data
        target = self.find(user.username)
        target.name, target.email = user.name, user.email
        
    def list_all(self):
        return self.users

database = UserDatabase()

database.insert(hemanth)
database.insert(aakash)
database.insert(siddhant)

user = database.find('siddhant')
print(user)

"""

QUESTION 2: Implement a binary tree using Python, and show its usage with some examples.
"""

print("\n-----------Question 2: Implement a binary tree using Python, and \
    show its usage with some examples.--------------\n")
# Here's a simple class representing a node within a binary tree.
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)

# Assign the node1 and node2 as the left and right of the node0
node0.left = node1
node0.right = node2

# Use the root object to represent the root of the tree
root = node0

print(f"The base node is {root.key}, where the \
left node is {root.left.key} & right node is {root.right.key}.")

# Create binary tree using tuple data
tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))

# create the tree by parsing the tuple
def parse_tuple(data):
    # check if the argument is tuple is its length is 3 so to add root, left and right nodes.
    # Else its a root node.
    if isinstance(data, tuple) and len(data) == 3:
        # create instance of the class
        node = TreeNode(data[1])
        # recursivly add the data
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    # add single node
    elif data is None:
        node = None
    else:
        # add root node
        node = TreeNode(data)
    return node

# now we need to display the tree from root
def display_keys(node, space='\t', level=0):
    
    # If the node is empty
    if node is None:
        print(space*level + '-')
        return   
    
    # If the node is a leaf 
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    
    # If the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left,space, level+1)

# call the method to create the binary tree
new_root = parse_tuple(tree_tuple)

# call this method to print the tree from left to right. means the root will be at right
print("\nDisplay the tree:")
display_keys(new_root)

print("\n-----------Question 3: Write a function to perform the inorder traversal \
of a binary tree.--------------\n")

def traverse_in_order(node):
    if node is None: 
        return []
    return(traverse_in_order(node.left) + 
           [node.key] + 
           traverse_in_order(node.right))

print(traverse_in_order(new_root))

print("\n-----------QUESTION 4: Write a function to perform the preorder traversal \
    of a binary tree.--------------\n")


def traverse_pre_order(node):
    if node is None: 
        return []
    return([node.key]+ 
            traverse_pre_order(node.left) + 
           traverse_pre_order(node.right))

print(traverse_pre_order(new_root))

print("\n-----------QUESTION 5: Write a function to perform the postorder traversal \
    of a binary tree.--------------\n")

def traverse_post_order(node):
    if node is None: 
        return []
    return(traverse_post_order(node.left) + 
           traverse_post_order(node.right)+
           [node.key])

print(traverse_post_order(new_root))

print("\n-----------QUESTION 6: Write a function to calculate the height/depth of \
a binary tree--------------\n")

def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left),tree_height(node.right))    
    

print("Height/depth of the tree: ",tree_height(new_root))

def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right) 

print("Number of nodes in the tree: ",tree_size(new_root)) 

def max_depth(node):
    if node is None:
        return 0
    return 1 + max(max_depth(node.left),max_depth(node.right))    
    

print("Max depth of the tree: ",max_depth(new_root))

def min_depth(node):
    if node is None:
        return 0
    return 1 + min(min_depth(node.left),min_depth(node.right))    
    

print("Min depth of the tree: ",min_depth(new_root))

def tree_diameter(node):
    if node is None:
        return 0

    
    # Get the height of left and right sub-trees
    left_node_height = tree_height(node.left)
    right_node_height = tree_height(node.right)

    # Get the diameter of left and right sub-trees
    left_node_diameter = tree_diameter(node.left)
    right_node_diameter = tree_diameter(node.right)

    # max between heigh of left, right & current node and diameter of left and right node.
    return max(left_node_height + right_node_height + 1, \
        max(left_node_diameter, right_node_diameter))       

print("Diameter of the tree: ",tree_diameter(new_root))

print("\n-----------QUESTION 8: Write a function to check if a binary tree is a binary \
search tree (BST). \nQUESTION 9: Write a function to find the maximum key in a binary tree.\
\nQUESTION 10: Write a function to find the minimum key in a binary tree.--------------\n")

def remove_none(nums):
    return [x for x in nums if x is not None]

def is_bst(node):
    if node is None:
        return True, None, None
    
    is_bst_left, min_left, max_left = is_bst(node.left)
    is_bst_right, min_right, max_right = is_bst(node.right)

    
    is_bst_node = (is_bst_left and is_bst_right and 
              (max_left is None or max_left < node.key) and 
              (min_right is None or min_right > node.key ))
    
    min_key = min(remove_none([min_left, node.key, min_right]))
    max_key = max(remove_none([max_left, node.key, max_right]))
    
    # print(node.key, min_key, max_key, is_bst_node)
        
    return is_bst_node, min_key, max_key

print("\nDisplay the tree:")
display_keys(new_root)
print(is_bst(new_root))

tree_tuple = ((1,1.5,None), 2, ((None, 3, 4), 5, (6, 7, 8)))

new_root = parse_tuple(tree_tuple)
print("\nDisplay the tree:")
display_keys(new_root)
print(is_bst(new_root))


print("\n-----------------------Storing Key-Value Pairs using BSTs------------------\n")
class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

tree = BSTNode(jadhesh.username, jadhesh)

tree.left = BSTNode(biraj.username, biraj)
tree.right = BSTNode(sonaksh.username, sonaksh)

tree.left.left = BSTNode(aakash.username, aakash)
tree.left.right = BSTNode(hemanth.username, hemanth)

tree.right.left = BSTNode(siddhant.username, siddhant)
tree.right.right = BSTNode(vishal.username, vishal)

display_keys(tree)

print("\n-----------QUESTION 11: Write a function to insert a new node into a BST.----\n")

def insert(node, key, value):
    # root node
    if node is None:
        node = BSTNode(key, value)
    # if key is less than the node key put it to the left of node vice-versa
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node

tree = insert(None, jadhesh.username, jadhesh)
insert(tree, sonaksh.username, sonaksh)
insert(tree, biraj.username, biraj)
insert(tree, aakash.username, aakash)
insert(tree, hemanth.username, hemanth)
insert(tree, siddhant.username, siddhant)
insert(tree, vishal.username, siddhant)
display_keys(tree)
