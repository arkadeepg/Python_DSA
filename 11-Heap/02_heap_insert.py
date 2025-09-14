H = __import__("01_heap")

my_heap = H.MaxHeap()

my_heap.insert(99)
my_heap.insert(72)
my_heap.insert(61)
my_heap.insert(58)

print(my_heap.heap)

my_heap.insert(100)

print(my_heap.heap)

my_heap.insert(75)

print(my_heap.heap)
