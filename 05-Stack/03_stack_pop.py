S = __import__("01_stack")

my_stack = S.Stack(6)

my_stack.push(4)
my_stack.print_stack()

my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.push(8)
my_stack.print_stack()