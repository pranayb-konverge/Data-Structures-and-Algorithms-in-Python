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

# get only non None nodes from the list
def remove_none(list_nums):
    return [x for x in list_nums if x is not None]

def is_bst(node):
    if node is None:
        return True, None, None
    
    # this recursive call will get the boolean value from the node's left and right.
    is_bst_left, min_left, max_left = is_bst(node.left)
    is_bst_right, min_right, max_right = is_bst(node.right)

    # get the boolean value
    is_bst_node = (is_bst_left and is_bst_right and 
              (max_left is None or max_left < node.key) and 
              (min_right is None or min_right > node.key ))
    # get the min and max nodes in the the whole tree
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
# This class will be useful to to represent the nodes of tree
# The node has its identity=key, data=value, left and right are the edges and 
# parent is to know who is the nodes parent
class BSTNode():
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, node, key, value):
        # root node
        if node is None:
            node = BSTNode(key, value)
        # if key is less than the node key put it to the left of node vice-versa
        elif key < node.key:
            node.left = self.insert(node.left, key, value)
            node.left.parent = node
        elif key > node.key:
            node.right = self.insert(node.right, key, value)
            node.right.parent = node
        return node

    def find(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node
        # if given key is less than the node's key it means we need to go left and vice-versa
        if key < node.key:
            return self.find(node.left, key)
        if key > node.key:
            return self.find(node.right, key)

    # find the value and update the target
    def update(self,node, key, value):
        target = self.find(node, key)
        if target is not None:
            target.value = value

    # get all the nodes in list
    def list_all(self,node):
        if node is None:
            return []
        # inorder way of listing all the nodes
        return self.list_all(node.left) + [(node.key, node.value)] + self.list_all(node.right)

    def is_balanced(self, node):
        if node is None:
            return True, 0
        # check if the left subtree is balanced
        balanced_left_node, height_left_node = self.is_balanced(node.left)
        # check if the right subtree is balanced
        balanced_right_node, height_right_node = self.is_balanced(node.right)
        # the difference between heights of left subtree and right subtree is not more than 1.
        # we need absolute number so abs() is used (right side is greater than left side)
        balanced = balanced_left_node and balanced_right_node and abs(height_left_node - height_right_node) <=1
        # get the height of the tree
        height = 1 + max(height_left_node, height_right_node)
        return balanced, height

    def make_balanced_bst(self, data, lo=0, hi=None, parent=None):
        if hi is None:
            # length of tree data list
            hi = len(data) - 1
        if lo > hi:
            # no data list is provided
            return None
        # get the middle element from the data list as root and set it as BSTNode root
        mid = (lo + hi) // 2
        # key=username and value=User obj
        key, value = data[mid]
        root = BSTNode(key, value)

        root.parent = parent
        # using reccursion we will create the left half of the tree and vice-versa
        # as per the binary search, to go left we need to do mid-1 and vice-versa in a list.
        root.left = self.make_balanced_bst(data, lo, mid-1, root)
        root.right = self.make_balanced_bst(data, mid+1, hi, root)
        
        return root

    def balance_bst(self,tree):
        return self.make_balanced_bst(self.list_all(tree))

# here we are defining the tree nodes with key,value and the edges (left-right nodes)
# this is without the insert method
tree = BSTNode(jadhesh.username, jadhesh)

tree.left = BSTNode(biraj.username, biraj)
tree.right = BSTNode(sonaksh.username, sonaksh)

tree.left.left = BSTNode(aakash.username, aakash)
tree.left.right = BSTNode(hemanth.username, hemanth)

tree.right.left = BSTNode(siddhant.username, siddhant)
tree.right.right = BSTNode(vishal.username, vishal)

display_keys(tree)

print("\n-----------QUESTION 11: Write a function to insert a new node into a BST.----\n")

# the None is for root node and this is created using the inser method
node_obj = BSTNode(None)
# this is the root node and we can call it as tree
tree = node_obj.insert(None, jadhesh.username, jadhesh)
node_obj.insert(tree, sonaksh.username, sonaksh)
node_obj.insert(tree, biraj.username, biraj)
node_obj.insert(tree, aakash.username, aakash)
node_obj.insert(tree, hemanth.username, hemanth)
node_obj.insert(tree, siddhant.username, siddhant)
node_obj.insert(tree, vishal.username, vishal)
display_keys(tree)

print("\n------QUESTION 11: Find the value associated with a given key in a BST.----\n")
node = node_obj.find(tree, "biraj")

print(f"Key: {node.key}, \nValue: {node.value}, \nLeft Node: {node.left}, \nRight Node: {node.right}")

print("\n--QUESTION 12: Write a function to update the value \
    associated with a given key within a BST--\n")

node = node_obj.find(tree, 'hemanth')
print("Before:")
print(f"Key: {node.key}, \nValue: {node.value}, \nLeft Node: {node.left}, \nRight Node: {node.right}")

# node, key, value
node_obj.update(tree, 'hemanth', User('hemanth', 'Hemanth Jinnar', 'hemanth.jinnar@example.com'))
node = node_obj.find(tree, 'hemanth')

print("\nAfter:")
print(f"Key: {node.key}, \nValue: {node.value}, \nLeft Node: {node.left}, \nRight Node: {node.right}")

print("\n--QUESTION 13: Write a function to retrieve all the key-values\
     pairs stored in a BST in the sorted order of keys.--\n")

print(node_obj.list_all(tree))

print("\n--QUESTION 14: Write a function to determine if a binary tree is balanced.--\n")
is_balanced = node_obj.is_balanced(tree)[0]
height = node_obj.is_balanced(tree)[1]
print(f"Is the tree balanced? {is_balanced}, height of tree? {height}")

print("\n--Exercise: Is the tree shown below balanced? Why or why not? \
    Create this tree and check if it's balanced using the is_balanced function.--\n")

tanya = User('tanya', 'Tanya Goel', 'tanya.g@example.com')
tree_new = node_obj.insert(tree, tanya.username, tanya)

# uuvi = User('uuvi', 'uuvi Goel', 'uuvi.g@example.com')
# tree_new = node_obj.insert(tree, uuvi.username, uuvi)

display_keys(tree_new)

is_balanced = node_obj.is_balanced(tree_new)[0]
height = node_obj.is_balanced(tree_new)[1]
print(f"Is the tree balanced? {is_balanced}, height of tree? {height}")
if is_balanced:
    print("""Why is it Balanced? \nAns: A binary tree in which the height of the left and 
    right subtree of any node differ by not more than 1. In this example, 
    only 'tanya' was added if she had another node in left or right, 
    it would be an imbalanced tree.""")
else:
    print("""Why is it not Balanced? \nAns: A binary tree in which the height of the left and 
    right subtree of any node differ by not more than 1. In this example, 
    only 'tanya' was added and she had another left node 'uuvi', which makes 
    the node diffrence to more than 1. So it is an imbalanced tree.""")

print("\n--QUESTION 15: Write a function to create a balanced \
    BST from a sorted list/array of key-value pairs--\n")

data = [(user.username, user) for user in users]
# print(data)
tree_new = node_obj.make_balanced_bst(data)
display_keys(tree_new)

print("\n--QUESTION 16: Write a function to balance an unbalanced binary search tree.--\n")

print("Unbalanced BST:")
tree_a = None
for user in users:
    tree_a = node_obj.insert(tree_a, user.username, user)
display_keys(tree_a)

print("Balanced BST:")
tree_b = node_obj.balance_bst(tree_a)
display_keys(tree_b)

print("\n----------------A Python-Friendly Treemap----------------\n")