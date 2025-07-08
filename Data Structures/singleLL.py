#single Linked List


class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            curr = self.head
            while curr.ref is not None:
                curr = curr.ref
            curr.ref = new_node

    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x==n.data:
                break
            n = n.ref
        if n is None:
            print("node is not presesnt in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node


    def print_LL(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

llist=LinkedList()
llist.add_end(5)
llist.add_end(4)
llist.add_end(7)
llist.add_end(9)
llist.add_end(10)
llist.add_end(1)
llist.add_end(9)
llist.add_begin(12) # add 12 at the beginning
llist.add_after(80, 10)
llist.print_LL() # print the linked list
