Q = __import__("01_queue")

my_queue = Q.Queue(4)

my_queue.enqueue(3)
my_queue.enqueue(7)
my_queue.print_queue()