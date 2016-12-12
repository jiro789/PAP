
class Dfs:

    def __init__(self, grafo):
        self.grafo = grafo
        self.discovered = [-1 for i in range(self.grafo.size())]
        self.visited = [False for i in range(self.grafo.size())]
        self.parents = [-1 for i in range(self.grafo.size())]
        self.low = [-1 for i in range(self.grafo.size())]
        self.time = 0
        self.is_bridge = {edge:False for edge in self.grafo.edges()}
        self.bridges = []
        self.number_components = 0
        self.components_of_node = [-1 for i in range(self.grafo.size())]
        self.size_of_component = 0
        self.size_of_components = []

    def run(self):
        for nodo in self.grafo.nodes():
            if not self.visited[nodo]:
                self.dfs_visit(nodo)
                self.number_components += 1
                self.size_of_components.append(self.size_of_component)
                self.size_of_component = 0

    def dfs_visit(self, u):
        self.visited[u] = True
        self.time += 1
        self.discovered[u] = self.time
        self.low[u] = self.time
        self.components_of_node[u] = self.number_components
        self.size_of_component += 1

        for v in self.grafo.neighbors(u):
            if not self.visited[v]:
                self.parents[v] = u
                self.dfs_visit(v)

                # actualizacion de low en caso de tree edge
                self.low[u] = min(self.low[u], self.low[v])

                # Condicion para bridge
                if self.low[v] > self.discovered[u]:
                    self.is_bridge[(u,v)] = True
                    self.is_bridge[(v,u)] = True
                    self.bridges.append((u,v))

            elif v != self.parents[u]:
                # actualizacion de low en caso de back edge
                self.low[u] = min(self.low[u], self.discovered[v])
