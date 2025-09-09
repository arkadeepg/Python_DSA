DLL = __import__("01_doubly_linked_list")

my_DLL = DLL.DoublyLinkedList(10)

my_DLL.append(12)
my_DLL.print_list()

my_DLL.append(5)
my_DLL.print_list()

my_DLL.pop()
my_DLL.pop()
my_DLL.pop()
my_DLL.print_list()

my_DLL.append(9)
my_DLL.print_list()
