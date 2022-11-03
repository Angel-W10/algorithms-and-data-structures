# linked list using python, 

# creating the Node class
class Node():
    # init function
    def __init__(self, value=None):
        self.value = value
        self.next = None

    
# creating the class for linked list that uses the node class as nodes in a linked list
class linked_list():
    # init function
    def __init__(self, value):
        self.head = Node(value)

    
    # function to insert values
    def insert_value(self, value):
        if(value == None):
            return False
        
        temp = self.head

        while(temp.next is not None):
            temp=temp.next
        
        temp.next = Node(value)

    # function to print the linked list
    def print_list(self):
        if(self.head):
            temp = self.head
            while(temp is not None):
                print(temp.value)
                temp = temp.next






if __name__ == "__main__":
    mylist = linked_list(10)
    mylist.insert_value(11)
    mylist.insert_value(12)
    mylist.insert_value(13)
    mylist.insert_value(14)


    mylist.print_list()