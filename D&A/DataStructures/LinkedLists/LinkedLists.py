{"value": 4, "next": None}

# !This is what a node essentially is but not exactly this.

# *So if we want to point Node 7 at Node 4 > This is kinda how it would it look
{"value": 7, "next": {"value": 4, "next": None}}

# head -> (11) -> (3) -> (23) -> (7) -> tail-> (4) (APPENDING 4)

head = {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {"value": 7, "next": {"value": 4, "next": None}},  # <-Tail
        },
    },
}

# print(head["next"]["next"]["value"]) #! Prints 23

# !!!!!! THIS IS HOW WE RUN AN ACTUAL LINKED LIST
# ?print(my_linked_list.head.next.next.value)


# ! WE DO THIS BECAUSE WE DONT WANT TO CREATE A NEW NODE ON EACH FUNCTION IN LINKED LIST CLASS !
# This will create a new NODE and replace the need for it to be created each time below
class Node:
    def __init__(self, value):
        # Just like we did above with the dictionary
        self.value = value
        self.next = None


class LinkedList:
    # The __init__ will create a new NODE and init a linked list
    def __init__(self, value):
        """
          We want to create the node
        ! at the time we create the linked list
          in this INIT
        """
        # This creates
        #! (4) -> None
        new_node = Node(value)
        # Then we declare it as the head
        #! head -> (4) -> None
        self.head = new_node
        # Then we declare it as the tail
        #! tail -> (4) -> None
        self.tail = new_node
        # We also have to track length so we start with 1 as the first node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # The append will create a new NODE and add it to the END
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        # Do not need this for append but need this for a true false used in a method down the line
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        pre = self.head
        temp = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    # The prepend will create a new NODE and add it to the FRONT
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    # The pop_first will pop off the first NODE 
    def pop_first(self):
        if self.length == 0:
            

    # The insert will create a new NODE and add it to the INDEX given
    def insert(self, index, value):
        print("inserted")


# my_linked_list creates the node, assigns it a value of 4 and does that tail and head functions as shown in the INIT
my_linked_list = LinkedList(9)
my_linked_list.append(1)
my_linked_list.append(3)
my_linked_list.pop().value
my_linked_list.prepend(2)
my_linked_list.prepend(3)
my_linked_list.pop_first().value
# my_linked_list.pop().value

my_linked_list.print_list()
print(f"Head is {my_linked_list.head.value}")
print(f"Tail is {my_linked_list.tail.value}")
print(f"Length is {my_linked_list.length}")
