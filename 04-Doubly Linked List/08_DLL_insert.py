DLL = __import__("01_doubly_linked_list")

my_DLL = DLL.DoublyLinkedList(10)

my_DLL.pop()
my_DLL.print_list()

my_DLL.insert(-1,7)
my_DLL.print_list()

my_DLL.insert(4,7)
my_DLL.print_list()

my_DLL.append(9)
my_DLL.insert(1,5)
my_DLL.print_list()

my_DLL.insert(0,3)
my_DLL.print_list()

my_DLL.insert(3,4)
my_DLL.print_list()

my_DLL.insert(8,12)
my_DLL.print_list()
