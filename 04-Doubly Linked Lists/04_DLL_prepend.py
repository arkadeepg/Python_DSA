DLL = __import__("01_doubly_linked_list")

my_DLL = DLL.DoublyLinkedList(10)

my_DLL.prepend(7)
my_DLL.print_list()

my_DLL.pop()
my_DLL.print_list()

print("\n###\n")

my_DLL.pop()
my_DLL.pop()
my_DLL.print_list()

my_DLL.prepend(12)
my_DLL.print_list()