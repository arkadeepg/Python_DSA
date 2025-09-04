class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node: Node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node: Node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self, value):
        new_node: Node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            temp = self.head
            self.head = new_node
            self.head.next = temp
            self.length += 1

    def pop(self):
        if self.length == 0:
            print("LL is empty")
        elif self.length == 1:
            print(f"Popped {self.head.value}")
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            temp = self.head
            while temp.next is not None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            print(f"Popped {temp.value}")

    def pop_first(self):
        if self.length == 0:
            print("LL is empty")
        elif self.length == 1:
            print(f"Popped {self.head.value}")
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            print(f"Popped {self.head.value}")
            self.head = self.head.next
            self.length -= 1

    def get_value(self, index):
        if index < 0 or index >= self.length:
            print("Index out of bound")
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            print(f"Got {temp.value}")

    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            print("Index out of bound")
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            temp.value = value

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            print("Index out of bound")
        elif index == 0:
            self.prepend(value)
        elif index == self.length-1:
            self.append(value)
        else:
            new_node: Node = Node(value)
            temp = self.head
            for _ in range(index-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            print("Index out of bound")
        elif index == 0:
            self.pop_first()
        elif index == self.length-1:
            self.pop()
        else:
            temp = self.head
            for _ in range(index):
                pre = temp
                temp = temp.next
            pre.next = temp.next
            self.length -= 1
            print(f"Removed {temp.value}")

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_linked_list: LinkedList = LinkedList(4)
my_linked_list.append(5)
my_linked_list.prepend(9)
my_linked_list.print_list()

my_linked_list.get_value(1)
my_linked_list.set_value(1,2)
my_linked_list.print_list()

my_linked_list.get_value(2)
my_linked_list.insert(2,7)
my_linked_list.print_list()

my_linked_list.pop()
my_linked_list.pop()
my_linked_list.pop()
my_linked_list.pop()
my_linked_list.pop()

my_linked_list.append(1)
my_linked_list.append(3)
my_linked_list.print_list()

my_linked_list.pop_first()
my_linked_list.print_list()
print("####")
my_linked_list.append(5)
my_linked_list.append(8)
my_linked_list.print_list()
my_linked_list.remove(2)
my_linked_list.print_list()