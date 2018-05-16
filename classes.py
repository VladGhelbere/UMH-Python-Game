#code for classes

from tkinter import *
import random

#one node from the linked list
class node:
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node

#linked list used for inventory
class linked_list:
    def __init__(self):
        self.cur_node = None

    def add_node(self, data):
        new_node = node() # create a new node
        new_node.data = data
        new_node.next = self.cur_node # link the new node to the 'previous' node.
        self.cur_node = new_node #  set the current node to the new one.

    def list_print(self,inventoryList):
        node = self.cur_node # cant point to ll!
        while node:
            inventoryList.insert(END, node.data)
            node = node.next

    def find_node(self,item):
        current = self.cur_node
        found = False
        while current != None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next
        return found

    def delete_list(self):
        self.cur_node = None