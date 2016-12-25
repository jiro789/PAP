import Grafo
from collections import namedtuple

Point = namedtuple('Point', ('x', 'y'))
Vector = namedtuple('Vector', ('x', 'y'))


# funciones ayudantes

def is_smaller(point1, point2):
    if point1.x < point2.x:
        return True
    elif point1.x == point2.x and point1.y < point2.y:
        return True
    else:
        return False


def find_smaller(vertices, funcion):
    assert (len(vertices) > 0), "no debería un self.polygon tener al menos un vertice ?"
    elem = vertices[0]
    for aComparar in vertices:
        if funcion(aComparar, elem):
            elem = aComparar
    return elem


def cross_product(vector1, vector2):
    # x1y2 − x2y1
    return vector1.x * vector2.y - vector2.x * vector1.y


def point_more_clockwise(originPoint, pointA, pointB):
    # retorna cual esta clockwise si b o c

    v1 = Vector(pointA.x - originPoint.x, pointA.y - originPoint.y)
    v2 = Vector(pointB.x - originPoint.x, pointB.y - originPoint.y)

    if cross_product(v1, v2) >= 0:
        return pointB
    else:
        return pointA


class Ejercicio1:
    def __init__(self):
        self.map_vertex_to_id = {}
        self.map_id_to_vertex = {}
        self.polygon = None
        self.parse_polygon()

    def solve(self):
        vertex_in_clockwise = self.polygon_vertexs_in_clockwise_order()
        print(*[str(self.map_id_to_vertex[x].x) + " " + str(self.map_id_to_vertex[x].y) for x in
                vertex_in_clockwise])

    def polygon_vertexs_in_clockwise_order(self):
        assert (self.polygon.number_of_nodes >= 3), "un self.polygon tiene al menos 3 vertices"

        first_point = find_smaller(list(self.map_vertex_to_id.keys()), is_smaller)

        index_first_point = self.map_vertex_to_id[first_point]

        p1, p2 = self.polygon.neighbors(index_first_point)

        more_clockwise_point = self.map_vertex_to_id[
            point_more_clockwise(first_point, self.map_id_to_vertex[p1], self.map_id_to_vertex[p2])]

        vertexs = list()

        vertexs.append(index_first_point)

        previous = index_first_point
        current = more_clockwise_point

        while current != index_first_point:
            vertexs.append(current)
            for vecino in self.polygon.neighbors(current):
                if vecino != previous:
                    previous = current
                    current = vecino
                    break

        return vertexs

    def parse_polygon(self):
        n = int(input())
        id_vertex = 0
        edges = set()
        for i in range(n - 2):

            l = list(map(int, input().split()))
            # agregar todos los vertices del triangulo
            v1 = Point(l[0], l[0 + 1])
            v2 = Point(l[2], l[2 + 1])
            v3 = Point(l[4], l[4 + 1])
            for v in (v1, v2, v3):
                if v not in self.map_vertex_to_id:
                    self.map_vertex_to_id[v] = id_vertex
                    self.map_id_to_vertex[id_vertex] = v
                    id_vertex += 1

            # creo las aristas finalmente

            # recupero id y ordeno para que las aristas tengan el id mas bajo a la izquierda
            vertices_l = [self.map_vertex_to_id[v1], self.map_vertex_to_id[v2], self.map_vertex_to_id[v3]]
            vertices_l.sort()
            e1 = vertices_l[0], vertices_l[1]
            e2 = vertices_l[0], vertices_l[2]
            e3 = vertices_l[1], vertices_l[2]

            for arista in (e1, e2, e3):
                if arista not in edges:
                    edges.add(arista)
                else:
                    edges.remove(arista)

        # creo el grafo a partir de las aristas

        self.polygon = Grafo.Grafo(n, n - 1)
        for arista in edges:
            self.polygon.add_edge(arista[0], arista[1])


ejercicio1 = Ejercicio1()
ejercicio1.solve()
