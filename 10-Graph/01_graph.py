class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            print("Added Vertex: ", vertex)
            return
        print("Vertex already present")

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            print("Edge added between", v1, "and", v2)
            return
        print("Vertices don't exist")

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
                print("Edge removed between", v1, "and", v2)
            except ValueError:
                pass
            return
        print("Vertices don't exist")

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for i in range(len(self.adj_list[vertex])):
                self.adj_list[self.adj_list[vertex][i]].remove(vertex)
            self.adj_list.pop(vertex)
            print("Vertex removed: ", vertex)
            return
        print("Vertex not found")

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])