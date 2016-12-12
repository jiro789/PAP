class Grafo:

    def __init__(self, n, m):
        self.number_of_nodes = n
        self.number_of_edges = m
        self.adjacency_list = [[] for i in range(n)]
        self._edges = []
        self.time = 0

    def size(self):
        return self.number_of_nodes

    def nodes(self):
        return [i for i in range(self.number_of_nodes)]

    def edges(self):
        return self._edges

    def add_edge(self, v1, v2):
        self.adjacency_list[v1].append(v2)
        self.adjacency_list[v2].append(v1)
        self._edges.append((v1, v2))

    def remove_edge(self, v1, v2):
        self.adjacency_list[v1].remove(v2)
        self.adjacency_list[v2].remove(v1)

        if (v1, v2) in self.edges():
            self._edges.remove((v1, v2))
        elif (v2, v1) in self.edges():
            self.edges.remove((v2, v1))

    def neighbors(self, u):
        return self.adjacency_list[u]

    def copy(self):
        nuevo_grafo = Grafo(self.number_of_nodes, self.number_of_edges)

        for edge in self.edges():
            u, v = edge
            nuevo_grafo.add_edge(u, v)

        return nuevo_grafo
