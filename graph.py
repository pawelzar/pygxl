class Node:
    def __init__(self, index, name='', attrs=''):
        self.index = index
        self.name = name
        self.attrs = attrs


class Edge:
    def __init__(self, index, name='', node_from='', node_to='', attrs=''):
        self.index = index
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
        """
        Construct incidence matrix of graph. Returns grid with described edge
        indices and node indices.
        """
        matrix = [
            [0 for _ in range(len(self.edges))] for _ in range(len(self.nodes))
        ]

        for node_id, node in enumerate(self.nodes):
            for edge_id, edge in enumerate(self.edges):
                if edge.node_from == node.index:
                    matrix[node_id][edge_id] = 1
                if edge.node_to == node.index:
                    matrix[node_id][edge_id] = -1

        for row_id, node in enumerate(self.nodes):
            matrix[row_id].insert(0, node.index)

        matrix.insert(0, [''] + [edge.index for edge in self.edges])

        return matrix

    def draw_incidence_matrix(self):
        """
        Prints the output of incidence matrix in a pleasing look.
        """
        for row in self.incidence_matrix:
            longest = len(max(
                [item.index for item in self.edges + self.nodes],
                key=len
            ))
            print(' '.join(
                '{:>{length}}'.format(item, length=longest) for item in row)
            )
