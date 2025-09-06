DLL = __import__("01_doubly_linked_list")

my_DLL = DLL.DoublyLinkedList(10)

my_DLL.pop_first()
my_DLL.print_list()
my_DLL.pop_first()
my_DLL.append(9)
my_DLL.append(7)
my_DLL.pop_first()
my_DLL.print_list()
