G = __import__("01_graph")

my_graph = G.Graph()

my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")

my_graph.add_edge("A", "B")
my_graph.add_edge("B", "D")
my_graph.add_edge("C", "D")
my_graph.add_edge("D", "A")
my_graph.add_edge("C", "A")

my_graph.print_graph()

my_graph.remove_vertex("D")

my_graph.print_graph()

my_graph.remove_vertex("D")
