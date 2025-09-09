BST = __import__("01_tree_BST")

my_BST = BST.BinarySearchTree()

my_BST.insert(4)
my_BST.insert(3)
my_BST.insert(5)

print(my_BST.root.value)
print(my_BST.root.left.value)
print(my_BST.root.right.value)
