class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def add_edges(v1,v2,v3):
    #ordeno los vertices
    v1,v2,v3 = sorted([v1,v2,v3])
    edge1 = (v1,v2);
    edge2 = (v1,v3);
    edge3 = (v2,v3);

def parse_input(id):
    n = int(input())
    for i in range(n-2):
        l = input().split()
        #agregar todos los vertices
        v1 = (l[0], l[0 + 1])
        v2 = (l[2], l[2 + 1])
        v3 = (l[4], l[4 + 1])
        for v in (v1,v2,v3):
            if v not in vertices_hasta_ahora:
                vertices[v] = id
                vertices_hasta_ahora.add(v)
                id += 1

        #creo las aristas finalmente

        vertices_l = [vertices[v1],vertices[v2],vertices[v3]]
        vertices_l.sort()
        e1 = vertices_l[0],vertices_l[1]
        e2 = vertices_l[0], vertices_l[2]
        e3 = vertices_l[1], vertices_l[2]
        print(vertices)
        print(e1,e2,e3)
        if e1 not in aristas:
            aristas.add(e1)
        else:
            aristas.remove(e1)
        if e2 not in aristas:
            aristas.add(e2)
        else:
            aristas.remove(e2)
        if e3 not in aristas:
            aristas.add(e3)
        else:
            aristas.remove(e3)

        print(aristas)

aristas = set()
vertices = {}
vertices_hasta_ahora = set()
id = 0

parse_input(id)


