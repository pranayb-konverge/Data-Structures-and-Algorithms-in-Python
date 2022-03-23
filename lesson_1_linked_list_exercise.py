print("\n-----------Write a function to print a linked list-------------\n")
"""
We'll implement linked lists which support the following operations:

1. Create a list with given elements
2. Display the elements in a list
3. Find the number of elements in a list
4. Retrieve the element at a given position
"""

# Create a class to add nodes of linked list
class Node():
    def __init__(self, number):
        self.data = number
        self.next = None

# add some nodes
node1 = Node(2)
node2 = Node(3)
node3 = Node(5)

print(f"Print the nodes {node1.data, node2.data, node3.data}")

# This calss will check the append, display elements 
# and get the lenght of LL and elements in LL
class LinkedList():
    def __init__(self):
        self.head = None
        
    def append_node(self, value):
        # if there is no node/head add one else 
        # assign the head of next node to current
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)
            
    def show_elements(self):
        current = self.head
        # get all the nodes
        while current is not None:
            print(current.data)
            current = current.next
            
    # get head count of all the nodes
    def length(self):
        result = 0
        current = self.head
        while current is not None:
            result += 1
            current = current.next
        return result
            
    # get node a a position in LL
    def get_element(self, position):
        i = 0
        current = self.head
        while current is not None:
            if i == position:
                return current.data
            current = current.next
            i += 1
        return None

first_list = LinkedList()
first_list.head = Node(2)
first_list.head.next = Node(3)
first_list.head.next.next = Node(4)

print(f"Display the linked list: \
{first_list.head.data, first_list.head.next.data, first_list.head.next.next.data}")

my_list = LinkedList()
my_list.append_node(2)
my_list.append_node(3)
my_list.append_node(5)
my_list.append_node(9)

print(f"Length of the linked list: {my_list.length()}.")
print(f"Print the element at position 3 of the linked list: {my_list.get_element(3)}.")
print(f"Get all the elements of the linked list:")
my_list.show_elements()

