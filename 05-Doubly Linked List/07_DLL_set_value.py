DLL = __import__("01_doubly_linked_list")

my_DLL = DLL.DoublyLinkedList(10)

my_DLL.append(9)
my_DLL.append(7)
my_DLL.append(6)

my_DLL.print_list()

my_DLL.set_value(-1,1)
my_DLL.print_list()

my_DLL.set_value(0,1)
my_DLL.print_list()

my_DLL.set_value(4,1)
my_DLL.print_list()

my_DLL.set_value(2,1)
my_DLL.print_list()
