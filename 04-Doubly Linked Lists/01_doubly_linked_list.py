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

if __name__ == "__main__":
    my_doubly_linked_list = DoublyLinkedList(2)
    my_doubly_linked_list.print_list()
    print("\n>>Append<<", end="")
    my_doubly_linked_list.append(5)
    my_doubly_linked_list.print_list()
    print("\n>>Pop<<")
    my_doubly_linked_list.pop()
    my_doubly_linked_list.print_list()

    my_doubly_linked_list.pop()
    my_doubly_linked_list.print_list()
    my_doubly_linked_list.pop()
    print("\n>>Prepend<<", end="")
    my_doubly_linked_list.prepend(3)
    my_doubly_linked_list.append(9)
    my_doubly_linked_list.prepend(1)
    my_doubly_linked_list.print_list()
    print("\n>>Get Value<<")
    my_doubly_linked_list.get_value(3)
    my_doubly_linked_list.get_value(1)
    print("\n>>Set Value<<", end="")
    my_doubly_linked_list.set_value(2,2)
    my_doubly_linked_list.print_list()
    print("\n>>Pop First<<")
    my_doubly_linked_list.pop_first()
    my_doubly_linked_list.print_list()
    my_doubly_linked_list.pop_first()
    my_doubly_linked_list.print_list()
    my_doubly_linked_list.pop_first()
    my_doubly_linked_list.print_list()
    my_doubly_linked_list.pop_first()
    print("\n>>Get Value<<")
    my_doubly_linked_list.get_value(1)
    print("\n>>Insert<<", end="")
    my_doubly_linked_list.insert(0,0)
    my_doubly_linked_list.insert(1,3)
    my_doubly_linked_list.insert(1,9)
    my_doubly_linked_list.print_list()
    my_doubly_linked_list.insert(1,1)
    my_doubly_linked_list.insert(2,2)
    my_doubly_linked_list.print_list()
    print("\n>>Remove<<")
    my_doubly_linked_list.remove(0)
    my_doubly_linked_list.remove(3)
    my_doubly_linked_list.remove(1)
    my_doubly_linked_list.remove(5)
    my_doubly_linked_list.print_list()
