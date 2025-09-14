H = __import__("01_heap")

my_heap = H.MaxHeap()

my_heap.remove()

my_heap.insert(99)
print(my_heap.heap)
my_heap.remove()
print(my_heap.heap)

my_heap.insert(95)
my_heap.insert(75)
my_heap.insert(80)
my_heap.insert(55)
my_heap.insert(60)
my_heap.insert(50)
my_heap.insert(65)
print(my_heap.heap)

my_heap.remove()
print(my_heap.heap)

my_heap.remove()
print(my_heap.heap)