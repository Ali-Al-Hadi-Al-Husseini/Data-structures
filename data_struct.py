"""
This library nade for people that are learning data structures, to help them if they face any problems
""""



# Linked lists Node class 
class Node:
  #initializing the node obect 
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node



# the linked list class the consist of  nodes objects
class LinkedList:
    def __init__(self, value=None):
        # if type(value) !=Node:
        self.head_node = value

    def get_head_node(self):

        return self.head_node
# parses through the linked list and inserts the new value after the specified index.
    def insert_after(self, index, new_value):
#         creating a new node with the  passed value
        node_to_insert = Node(new_value)
        current_node = self.get_head_node()
#makes the current_node variable the node at the passed  index
        for i in range(index-1):
            current_node = current_node.get_next_node()

        node_to_insert.set_next_node(current_node.next_node)
        current_node.set_next_node(node_to_insert)
# inserting a value at the begning of the linked 
    def insert_beginning(self, new_value):

        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
        
    """ this function return a string representation of the linked list in the following form 
        
        "0.first_node_value
          1.2nd_node_value
          2.3rd_node_value"
          
        the number represents the index od each node
              
    
    """
    def stringify_list(self):

        string_list = ""
        current_node = self.get_head_node()
        num = 0
        #parses through the hole linkedlist so wen can add all the node to the variable string_list
        while current_node:

              string_list += "{}-".format(num) + \
                  str(current_node.get_value()) + "\n"
              num += 1

            current_node = current_node.get_next_node()

        return string_list
      
#parses through the list until the value is found
    def remove_node(self, value_to_remove):

        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:

            self.head_node = current_node.get_next_node()
        else:

            while current_node:
                next_node = current_node.get_next_node()

                if next_node.get_value() == value_to_remove:

                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node

    def get_last_node(self):
        curr = self.get_head_node()

        while curr.get_next_node():
            curr = curr.get_next_node()

        return curr
      
    # adds anode at the end of the list just like append in normal lists

    def add_node(self, value):

        self.get_last_node().set_next_node(Node(value))

    def get_length(self):
        current_node = self.head_node
        counter = 1
        while current_node.get_next_node():
            counter += 1
            current_node = current_node.next_node
        return counter

    def reverse(self):
        curr = self.get_head_node()
        prev = None

        while curr:
            temp = curr.get_next_node()
            curr.set_next_node(prev)
            prev = curr
            curr = temp

        self.head_node = prev


