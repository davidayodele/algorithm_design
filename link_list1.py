# node class used to create node instances 
class node:
    # self (can technically be any word) is used bc in Python, the instance of a method is passed but not sutomatically received
    def __init__(self, data = None): # constructor with self as 1st arg, initializes data to null
        self.data = data # creates var to store data
        self.nex = None # creates var to store something (allows it to store nodes)


class link_list:
    def __init__(self, data=None): # constructor will be initialized with another class (node) to create a chain of nodes
        self.head = node(data) # creates variable called "head" to store 1st node in list, 1st node is null

    def append(self, data): # method for adding nodes to list
        curr_node = self.head  # creates a var to store current node
        new_node = node(data) # creates a new instance of node with data as input
        while curr_node.nex != None: # while not at end of list...
            curr_node = curr_node.nex # sets curr_node to something other than data (that can hold next node)
        curr_node.nex = new_node # store new node in curr_node.nex, creates iterator operation

    def erase(self, index): # method for removing a node
        if index >= self.length():
            print("Error: index out of range.")
            return
        curr_index = 0
        curr_node = self.head
        while curr_node.nex != None: # if node exists and contains target data...
            last_node = curr_node  # stores last node as curr_node
            curr_node = curr_node.nex # sets curr_node to next node
            if curr_index == index: # checks index of node
                temp = curr_node.data # stores data for possible extracting
                last_node.nex = curr_node.nex # erases curr_node by joining ends of prev and next node
                return temp # outputs erased data
            curr_index += 1
        return temp

    def insert_before(self, index, data): # method for inserting before any node
        if index - 1 >= self.length() or index - 1 < 0:
            print("Error: index out of range.")
            return
        new_node = node(data)
        curr_index = 0
        curr_node = self.head
        while curr_node.nex != None:
          if curr_index == index - 1:
            prev_node = curr_node
          curr_node = curr_node.nex
          curr_index += 1

        new_node.nex = prev_node.nex # sets next of new node to next of prev node 
        prev_node.nex = new_node # sets next of prev node to new node


    def length(self): # method for calculating list length
        curr_node = self.head # start at back of list
        length = 0
        while curr_node.nex != None: 
            curr_node = curr_node.nex
            length += 1
        return length

    def get(self, index): # method for getting a node
        if index >= self.length():
            print("Error: 'Get' index out of range.")
            return None
        curr_index = 0
        curr_node = self.head
        while curr_node.nex != None:
            curr_node = curr_node.nex 
            if curr_index == index:
                return curr_node.data
            curr_index += 1
    
    def display(self): # method for displaying list
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
new_list.append(7)
new_list.append(9)
print(new_list.erase(1))
print(new_list.get(2))
new_list.display()
print(new_list.length())
