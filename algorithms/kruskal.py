PARENT = dict()
RANK = dict()


def make_set(vertice):
    PARENT[vertice] = vertice
    RANK[vertice] = 0


def find(vertice):
    if PARENT[vertice] != vertice:
        PARENT[vertice] = find(PARENT[vertice])
    return PARENT[vertice]


def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if RANK[root1] > RANK[root2]:
            PARENT[root2] = root1
        else:
            PARENT[root1] = root2
            if RANK[root1] == RANK[root2]:
                RANK[root2] += 1


def kruskal(graph):
    for vertice in graph['nodes']:
        make_set(vertice)

    minimum_spanning_tree = set()
    edges = sorted(graph['edges'], key=lambda x: x[2])
    print('Kruakal\'s algorithm: ', edges)

    for edge in edges:
        vertice1, vertice2, _ = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)

    return minimum_spanning_tree
