LL = __import__("01_linked_list")

my_LL = LL.LinkedList(10)

my_LL.prepend(4)
my_LL.print_list()

my_LL.pop()
my_LL.pop()
my_LL.prepend(8)
my_LL.print_list()

my_LL.prepend(6)
my_LL.prepend(7)
my_LL.print_list()
