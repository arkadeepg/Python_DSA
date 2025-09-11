class HashMap:
    def __init__(self, size = 7):       # 7 or any prime number to reduce collision
        self.data_map = [None] * size

    def __hash__(self, key):        # Hash Function
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)     # 23 or any prime number
        return my_hash
    
    def set_item(self, key, value):
        index = self.__hash__(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash__(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    print(self.data_map[index][i][1])
                    return
        print("Not Found")

    def keys(self):
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    print(self.data_map[i][j][0])

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)
