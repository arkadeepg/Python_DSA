class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def reversal(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_linked_list: LinkedList = LinkedList(4)
my_linked_list.append(5)
my_linked_list.append(9)
my_linked_list.append(3)
my_linked_list.append(2)
my_linked_list.print_list()

print("#########")

my_linked_list.reversal()
my_linked_list.print_list()