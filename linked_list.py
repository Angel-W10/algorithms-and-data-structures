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

    # function to delete a value if its in the list
    # check if in the list
    # temp to the value
    # value->next = link
    # temp ->next = link
    def delete_value(self, value):
        if(value==None):
            return False

        if(self.head):
            temp = self.head
            while(temp.next.value is not value):
                temp = temp.next
            link = temp.next.next
            temp.next = link

    # function to print the linked list
    def print_list(self):
        if(self.head):
            temp = self.head
            while(temp is not None):
                # print(temp.value)
                print("%d -> " %temp.value, end="")
                temp = temp.next
            print("None\n")




if __name__ == "__main__":
    mylist = linked_list(10)
    mylist.insert_value(11)
    mylist.insert_value(12)
    mylist.insert_value(13)
    mylist.insert_value(14)

    print("old")
    mylist.print_list()

    mylist.delete_value(12)
    mylist.delete_value(13)
    print("new")
    mylist.print_list()