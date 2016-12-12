from collections import deque


class Bfs:

    def __init__(self, grafo):
        self.grafo = grafo
        self.distance = [-1 for nodo in range(grafo.number_of_nodes)]
        self.visited = [False for nodo in range(grafo.number_of_nodes)]

    def run(self, nodo):

        self.distance[nodo] = 0
        self.visited[nodo] = True
        cola = deque()
        cola.append(nodo)

        while len(cola) != 0:
            u = cola.popleft()
            for v in self.grafo.neighbors(u):
                if not self.visited[v]:
                    self.visited[v] = True
                    self.distance[v] = self.distance[u] + 1
                    cola.append(v)
