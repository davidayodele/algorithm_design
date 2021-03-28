# node class used to create node instances 
class node:
    # self (can technically be any word) is used bc in Python, the instance of a method is passed but not sutomatically received
    def __init__(self, data = None): # constructor with self as 1st arg, initializes data to null
        self.data = data # creates var to store data
        self.nex = None # creates var to store something (this allows it to store nodes)


class link_list:
    def __init__(self): # constructor will be initialized with another class (node) to create a chain of nodes
        self.head = node() # creates variable called "head" to store 1st node in list, 1st node is null

    def append(self, data): # method for adding nodes to list
        curr_node = self.head  # creates a var to store 1st node
        new_node = node(data) # creates a new instance of node with data as input
        while curr_node.nex != None: # while not at end of list...
            curr_node = curr_node.nex # sets curr_node to something other than data (that can hold next node)
        curr_node.nex = new_node # store new node in curr_node.nex, creates iterator operation

    def delete(self, data): # method for removing nodes from list
        curr_node = self.head  # creates a var to store 1st node
        
        # Head node case
        if curr_node == True and curr_node.data == data: # if node exists and contains target data...
            self.head = curr_node.nex # sets curr_node to next node, GC will handle unused data
            curr_node = None

        # General node case
        while curr_node.nex != None: # while not at end of list...
            if curr_node.data == data:
                curr_node = curr_node.nex # sets curr_node to next node, GC will handle unused data

    def prepend(self, data): # method for addding a new start node
        new_node = node(data) # creates new node
        new_node.nex = self.head # sets front link to head node 
        self.head = new_node # sets head to new node (replaces prev head)
    
    def insert_after(self, node, data): # method for inserting a node after another
        if not node:
            print("Node not in list")
            return
        new_node = node(data)
        node.nex = new_node
        new_node.nex = node.nex

    def length(self): # method for calculating list length
        curr_node = self.head # start at back of list
        length = 0
        while curr_node.nex != None: 
            curr_node = curr_node.nex
            length += 1
        return length
    
    def display(self):
        items = []
        curr_node = self.head
        while curr_node.nex != None:
            curr_node = curr_node.nex
            items.append(curr_node.data)
        print(items)


# Main
new_list = link_list()
new_list.append(4)
new_list.append(5)
new_list.display()
print(new_list.length())
