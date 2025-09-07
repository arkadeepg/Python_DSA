DLL = __import__("01_doubly_linked_list")

my_DLL = DLL.DoublyLinkedList(10)

my_DLL.append(12)
my_DLL.print_list()

my_DLL.pop()
my_DLL.print_list()         # 2 items in list

my_DLL.pop()
my_DLL.print_list()         # 1 item in list

print("\n###\n")

my_DLL.pop()
my_DLL.print_list()         # 0 item in list
