class Node:
    def __init__(self, index, name='', attr=''):
        self.index = index
        self.name = name
        self.attr = attr


class Edge:
    def __init__(self, index, name='', node_from='', node_to='', attr=''):
        self.index = index
        self.name = name
        self.node_from = node_from
        self.node_to = node_to
        self.attr = attr


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

        return matrix

    @property
    def incidence_matrix_str(self):
        """
        Returns the output of incidence matrix in a pleasing look.
        """
        longest_node_id = len(max([n.index for n in self.nodes], key=len))
        longest_edge_id = len(max([e.index for e in self.edges], key=len))
        spacing = max(longest_edge_id + 1, 3)

        matrix = list()
        matrix.append(''.join(
            ['{:>{}}'.format('', longest_node_id)] +
            ['{:>{}}'.format(e.index, spacing) for e in self.edges]
        ))

        for i, row in enumerate(self.incidence_matrix):
            matrix.append(''.join(
                ['{:>{}}'.format(self.nodes[i].index, longest_node_id)] +
                ['{:>{}}'.format(value, spacing) for value in row]
            ))

        return matrix
