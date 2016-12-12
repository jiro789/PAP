import Grafo
import Dfs
import sys
import Bfs


class Ejercicio3:

    def __init__(self):
        self.grafo_inicial = None
        self.grafo_final = None
        self.grafo_componentes = None
        self.queries = []
        self.dfs_inicial = None
        self.dfs_final = None

    def create_from_file(self, aTextFile):
        file_input = open(aTextFile)

        n, m = [int(x) for x in file_input.readline().split()]

        grafo_inicial = Grafo.Grafo(n, m)
        grafo_final = Grafo.Grafo(n, m)

        for street in range(m):
            u, v = [int(x) for x in file_input.readline().split()]
            # nodos ahora de 0 a N-1
            u -= 1
            v -= 1
            grafo_inicial.add_edge(u, v)
            grafo_final.add_edge(u, v)

        q = int(file_input.readline())

        for query in range(q):
            self.queries.append([x for x in file_input.readline().split()])

        self.grafo_inicial = grafo_inicial
        self.grafo_final = grafo_final

    def prepare(self):

        #corrida del primer dfs
        dfs_inicial = Dfs.Dfs(self.grafo_inicial)
        dfs_inicial.run()

        #corto los ejes puente y corro el segundo dfs
        edges_to_cut = dfs_inicial.bridges

        for edge in edges_to_cut:
            u, v = edge
            self.grafo_final.remove_edge(u, v)

        dfs_final = Dfs.Dfs(self.grafo_final)
        dfs_final.run()

        self.dfs_inicial = dfs_inicial
        self.dfs_final = dfs_final

        # ahora creo un grafo de las componentes conexas ...
        grafoConexas = Grafo.Grafo(len(self.dfs_final.size_of_components), len(dfs_inicial.bridges))

        for edge in edges_to_cut:
            u, v = edge
            grafoConexas.add_edge(dfs_final.components_of_node[u], dfs_final.components_of_node[v])

        self.grafo_componentes = grafoConexas

    def solve(self):

        self.prepare()

        for query in self.queries:
            self.solve_query(query)

    def solve_query(self, query):
        header = query[0]
        result = None
        if header == 'A':
            result = self.solve_a(int(query[1]), int(query[2]))
        elif header == 'B':
            result = self.solve_b(int(query[1]))
        elif header == 'C':
            result = self.solve_c(int(query[1]))

        print(result)

    def solve_a(self, e1, e2):
        e1 -= 1
        e2 -= 1

        componente_inicio = self.dfs_final.components_of_node[e1]
        componente_final = self.dfs_final.components_of_node[e2]

        #computo las distancias entre los nodos en el grafo de componentes
        bfs = Bfs.Bfs(self.grafo_componentes)
        bfs.run(componente_inicio)

        return bfs.distance[componente_final]

    def solve_b(self, s1):
        s1 -= 1
        street = self.grafo_inicial.edges()[s1]

        if self.dfs_inicial.is_bridge[street]:
                return 1
        return 0

    def solve_c(self, esquina):
        esquina -= 1
        numero_componente = self.dfs_final.components_of_node[esquina]
        return self.dfs_final.size_of_components[numero_componente] - 1

ejercicio3 = Ejercicio3()
ejercicio3.create_from_file(sys.argv[1])
ejercicio3.solve()
