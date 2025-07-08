#Double Linked List


# define a class for the node object
class node:
    # initialize the node with data and pointers
    def __init__(self,data):
        self.data=data # the data stored in the node
        self.prev=None # the pointer to the previous node
        self.next=None # the pointer to the next node

# define a class for the double linked list object
class DLL:
    # initialize the list with head and tail pointers
    def __init__(self):
        self.head=None # the pointer to the first node
        self.tail=None # the pointer to the last node

    # define a method to add a new node at the end of the list
    def add_newnode(self,data):
        new_node=node(data) # create a new node with the given data
        if (self.head==None): # if the list is empty
            self.head=self.tail=new_node # set both head and tail to the new node
            self.head.prev=None # set the prev pointer of the head to None
            self.tail.next=None # set the next pointer of the tail to None
        else: # if the list is not empty
            self.tail.next=new_node # set the next pointer of the tail to the new node
            new_node.prev=self.tail # set the prev pointer of the new node to the tail
            self.tail=new_node # update the tail to the new node
            self.tail.next=None # set the next pointer of the tail to None
        return new_node
    # define a method to display the nodes of the list
    def display(self):
        current=self.head # start from the head node
        if(self.head==None): # if the list is empty
            print("list is empty") # print a message
            return # exit the method
        print("nodes of the double linked list are:") # print a header
        while(current.next!=None): # loop until reaching the last node
            print(current.data) # print the data of the current node
            current=current.next # move to the next node
        print(current.data) # print the data of the last node

    # define a method to add all the integer data of the nodes
    def sum(self):
        sum=0 # initialize the sum variable to zero
        if(self.head==None): # if the list is empty
            print("list is empty") # print a message
            sum=0 # initialize the sum variable to zero
            print("sum=",sum)
            return # exit the method
        current=self.head # set the current node to the head node
        while(current.next!=None):# loop until reaching the last node
            if isinstance(current.data,int):  # check if the data of the current node is an integer
                sum+=current.data # add it to the sum
            current=current.next # move to the next node
        if isinstance(current.data,int): # check if the data of the last node is an integer
            sum+=current.data # add it to the sum
        print("the sum of all nodes: ", sum) # print the final sum
    
    # define a method to push/ insert the node at the front/start of the list
    def push(self, newdata): 
        newnode=node(data=newdata) # create a new node with the given data
        newnode.next=self.head # set the next pointer of the new node to the head node
        newnode.prev=None # set the prev pointer of the new node to None
        if self.head is not None: # if the list is not empty
            self.head.prev=newnode # set the prev pointer of the head node to the new node's data
        self.head=newnode # update the head node to the new node
    
    # define a method to insert the node after the given previous node of the list 
    def insert(self, prevnode, newdata):
        if (prevnode is None): # if the previous node is None
            print("the previous node doesnot exist")
            return # exit the method
        newnode=node(data=newdata) # create a new node with the given data
        newnode.next=prevnode.next # set the next pointer of the new node to the next pointer of the previous node
        prevnode.next=newnode # set the next pointer of the previous node to the new node
        newnode.prev=prevnode # set the prev pointer of the new node to the previous node
        if newnode.next is not None: # if the new node is not the last node
            newnode.next.prev=newnode # set the prev pointer of the next node to the new node
    
    #define a method to insert the node at the end of the list after traversal to the end
    def append(self, newdata):
        newnode=node(data=newdata) # create a new node with the given data
        last=self.head # set the last node to the head node
        newnode.next=None # set the next pointer of the new node to None since it will be the last node
        if (self.head is None):  # if the list is empty
            print("the list is empty") # print a message
            newnode.prev=None # set the prev pointer of the new node to None
            self.head=newnode # set the head node to the new node
            return  # exit the method
        while(last.next is not None): # loop until reaching the last node
            last=last.next # move to the next node
        last.next=newnode # set the next pointer of the last node to the new node
        newnode.prev=last # set the prev pointer of the new node to the last node
        

# create an instance of DLL class
ddl=DLL()
# add some nodes to it
ddl.add_newnode(2)
previousnode=ddl.add_newnode(3)
ddl.add_newnode(4)
ddl.add_newnode(1)
ddl.add_newnode("string node")
#push the new node at the front of list (at start)
ddl.push(7)
#insert the new node after the previous node
ddl.insert(previousnode,8)
#insert the new node at the end of the list after traversing self.head till the end
ddl.append(9)
#sum of int data of nodes
ddl.sum()
# display them
ddl.display()









            