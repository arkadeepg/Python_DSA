LL = __import__("01_linked_list")

my_LL = LL.LinkedList(10)

my_LL.remove(0)
my_LL.remove(0)

my_LL.append(3)
my_LL.append(6)
my_LL.append(9)
my_LL.append(8)
my_LL.print_list()

my_LL.remove(-1)
my_LL.remove(7)
my_LL.print_list()

my_LL.remove(2)
my_LL.print_list()

my_LL.remove(3)
my_LL.print_list()
