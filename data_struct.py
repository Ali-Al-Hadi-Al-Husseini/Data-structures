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
        
#  a Node class that has two pointer, the first  points to the previous Double_node and the second  points to the next_node     
        
class Double_Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def set_prev_node(self, prev_node):
        self.prev_node = prev_node

    def get_prev_node(self):
        return self.prev_node

    def get_value(self):
        return self.value


class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def add_to_head(self, new_value):
        new_head = Double_Node(new_value)
        current_head = self.head_node

        if current_head != None:
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)

        self.head_node = new_head

        if self.tail_node == None:
            self.tail_node = new_head

    def add_to_tail(self, new_value):
        new_tail = Double_Node(new_value)
        current_tail = self.tail_node

        if current_tail != None:
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)

        self.tail_node = new_tail

        if self.head_node == None:
            self.head_node = new_tail

    def remove_head(self):
        removed_head = self.head_node

        if removed_head == None:
            return None

        self.head_node = removed_head.get_next_node()

        if self.head_node != None:
            self.head_node.set_prev_node(None)

        if removed_head == self.tail_node:
            self.remove_tail()

        return removed_head.get_value()

    def remove_tail(self):
        removed_tail = self.tail_node

        if removed_tail == None:
            return None

        self.tail_node = removed_tail.get_prev_node()

        if self.tail_node != None:
            self.tail_node.set_next_node(None)

        if removed_tail == self.head_node:
            self.remove_head()

        return removed_tail.get_value()

    def remove_by_value(self, value_to_remove):
        node_to_remove = None
        current_node = self.head_node

        while current_node != None:
            if current_node.get_value() == value_to_remove:
                node_to_remove = current_node
                break

            current_node = current_node.get_next_node()

        if node_to_remove == None:
            return None

        if node_to_remove == self.head_node:
            self.remove_head()
        elif node_to_remove == self.tail_node:
            self.remove_tail()
        else:
            next_node = node_to_remove.get_next_node()
            prev_node = node_to_remove.get_prev_node()
            next_node.set_prev_node(prev_node)
            prev_node.set_next_node(next_node)

        return node_to_remove

    def stringify_list(self):
        string_list = ""
        current_node = self.head_node
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list


class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0
        self.limit = limit

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
            print("Adding {} to the pizza stack!".format(value))
        else:
            print("No room for {}!".format(value))

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
 
            return item_to_remove.get_value()

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0    

class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            print("Adding " + str(item_to_add.get_value()) + " to the queue!")
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("Sorry, no more room!")

    def dequeue(self):
        if self.get_size() > 0:
            item_to_remove = self.head
            print(str(item_to_remove.get_value()) + " is served!")
            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            return None

    def look_at_top(self):
        if self.is_empty():
            return None
        else:
            return self.head.get_value()

    def get_size(self):
        return self.size

    def has_space(self):
        if self.max_size == None:
            return True
        else:
            return self.max_size > self.get_size()

    def is_empty(self):
        return self.size == 0
class TreeNode:
    def __init__(self, value):
        self.value = value  # data
        self.children = []  # references to other nodes

    def add_child(self, child_node):
        # creates parent-child relationship
        print("Adding " + child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        # removes parent-child relationship
        print("Removing " + child_node.value + " from " + self.value)
        self.children = [child for child in self.children
                         if child is not child_node]

    def traverse(self):
        # moves through each node referenced from self downwards
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children


class BinarySearchTree:
    def __init__(self, value, depth=1):
        self.value = value
        self.depth = depth
        self.left = None
        self.right = None

    def insert(self, value):
        if (value < self.value):
            if (self.left is None):
                self.left = BinarySearchTree(value, self.depth + 1)

            else:
                self.left.insert(value)
        else:
            if (self.right is None):
                self.right = BinarySearchTree(value, self.depth + 1)
  
            else:
                self.right.insert(value)

    def get_node_by_value(self, value):
        if (self.value == value):
            return self
        elif ((self.left is not None) and (value < self.value)):
            return self.left.get_node_by_value(value)
        elif ((self.right is not None) and (value >= self.value)):
            return self.right.get_node_by_value(value)
        else:
            return None

    def depth_first_traversal(self):
        if (self.left is not None):
            self.left.depth_first_traversal()

        if (self.right is not None):
            self.right.depth_first_traversal()

    def invertTree(self):
        if self is None:
            return None
        self.right, self.left = self.left, self.right
        self.right.invertTree()
        self.left.invertTree()
