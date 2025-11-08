class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.front = new_node
        self.rear = new_node
        self.length = 1

    # O(1) Constant time
    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.length += 1

    # O(1) Constant time
    def dequeue(self):
        if self.length == 0:
            print("Queue is empty")
            return
        temp = self.front
        if self.length == 1:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        print(f"Removed {temp.value}")
        self.length -= 1

    def print_queue(self):
        temp = self.front
        while temp is not None:
            print(temp.value)
            temp = temp.next
