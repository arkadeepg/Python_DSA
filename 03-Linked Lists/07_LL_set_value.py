LL = __import__("01_linked_list")

my_LL = LL.LinkedList(10)

my_LL.set_value(0,7)
my_LL.print_list()

my_LL.set_value(-1,2)
my_LL.print_list()
my_LL.set_value(1,2)
my_LL.print_list()

print("###")
my_LL.append(9)
my_LL.append(5)
my_LL.set_value(1,2)
my_LL.print_list()
print("###")
my_LL.set_value(2,9)
my_LL.print_list()
print(f">>{my_LL.length}<<")
my_LL.set_value(3,22)
my_LL.print_list()
