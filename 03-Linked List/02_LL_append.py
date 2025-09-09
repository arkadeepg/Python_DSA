LL = __import__("01_linked_list")

my_LL = LL.LinkedList(10)

my_LL.append(12)
my_LL.print_list()

my_LL.pop()
my_LL.pop()
my_LL.append(2)
my_LL.print_list()
