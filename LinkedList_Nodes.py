# Node class
class Node:

    # Function to initialize the node object
    def __init__(self, data):
        # Assign data
        self.data = data
        # Initialize next as nul
        self.next = None


class LinkedList:
    
    # Function to initialize the Linked 
    # List object
    def __init__(self):
        self.head = None
