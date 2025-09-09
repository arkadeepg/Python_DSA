class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return
            if new_node.value < temp.value:
                if temp.left == None:
                    temp.left = new_node
                    return
                temp = temp.left
            else:
                if temp.right == None:
                    temp.right = new_node
                    return
                temp = temp.right

    def contains(self, value):
        if self.root == None:
            print("Empty Tree")
            return
        temp = self.root
        while (temp is not None):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                print(f"{value} Found")
                return
        print(f"{value} Not Found")
