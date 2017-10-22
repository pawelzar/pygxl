class Node:
    def __init__(self, id, name, attrs):
        self.id = id
        self.name = name
        self.attrs = attrs


class Edge:
    def __init__(self, id, name, node_from, node_to, attrs):
        self.id = id
        self.name = name
        self.node_from = node_from
        self.node_to = node_to
        self.attrs = attrs


class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

    @property
    def incidence_matrix(self):
        return []

    def draw_incidence_matrix():
        for row in self.incidence_matrix:
            print(' '.join(row))
