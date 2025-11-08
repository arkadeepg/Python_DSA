class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # O(1) Constant time
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    # O(1) Constant time
    def pop(self):
        if self.length == 0:
            print("DLL is empty")
            return
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        print(f"Popped {temp.value}")

    # O(1) Constant time
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    # O(1) Constant time
    def pop_first(self):
        if self.length == 0:
            print("DLL is empty")
            return
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        print(f"Popped {temp.value}")

    # O(n) Linear time
    def get_value(self, index):
        if index < 0 or index >= self.length:
            print("Index out of bound")
        else:
            if index < self.length//2:
                temp = self.head
                for _ in range(index):
                    temp = temp.next
            else:
                temp = self.tail
                for _ in range(self.length-1, index, -1):
                    temp = temp.prev
            print(temp.value)

    # O(n) Linear time
    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            print("Index out of bound")
        else:
            if index < self.length//2:
                temp = self.head
                for _ in range(index):
                    temp = temp.next
            else:
                temp = self.tail
                for _ in range(self.length-1, index, -1):
                    temp = temp.prev
            temp.value = value

    # O(n) Linear time
    def insert(self, index, value):
        if index < 0:
            print("Index out of bound")
        elif index == 0:
            self.prepend(value)
        elif index >= self.length:
            self.append(value)
        else:
            if index < self.length//2:
                temp = self.head
                for _ in range(index):
                    temp = temp.next
            else:
                temp = self.tail
                for _ in range(self.length-1, index, -1):
                    temp = temp.prev
            new_node = Node(value)
            before = temp.prev
            before.next = new_node
            new_node.prev = before
            new_node.next = temp
            temp.prev = new_node
            self.length += 1

    # O(n) Linear time
    def remove(self, index):
        if index < 0 or index >= self.length:
            print("Index out of bound")
        elif index == 0:
            self.pop_first()
        elif index == self.length-1:
            self.pop()
        else:
            if index < self.length//2:
                temp = self.head
                for _ in range(index):
                    temp = temp.next
            else:
                temp = self.tail
                for _ in range(self.length-1, index, -1):
                    temp = temp.prev
            before = temp.prev
            after = temp.next
            before.next = after
            after.prev = before
            self.length -= 1

    def print_list(self):
        print(f"\n#{self.length}#")
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
