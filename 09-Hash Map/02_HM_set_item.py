HM = __import__("01_hash_map")

my_hash_map = HM.HashMap()

my_hash_map.set_item("bolts", 100)
my_hash_map.set_item("screws", 100)
my_hash_map.set_item("washers", 50)
my_hash_map.set_item("lumber", 20)

my_hash_map.print_table()
