class Node:
    def __init__(self, index, attr={}):
        self.index = index
        self.attr = attr

    def __str__(self):
        return self.index


class Edge:
    def __init__(self, index, node_from='', node_to='', attr={}):
        self.index = index
        self.node_from = node_from
        self.node_to = node_to
        self.attr = attr

    def __str__(self):
        return self.index


class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.incidence_matrix = self._create_incidence_matrix()

    def _create_incidence_matrix(self):
        """
        Constructs incidence matrix of graph.
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
        edge_ids = [e.index for e in self.edges]
        longest_edge_id = len(max(edge_ids, key=len))
        longest_node_id = len(max([n.index for n in self.nodes], key=len))
        spacing = max(longest_edge_id + 1, 3)

        def line(index, values):
            return (''.join(
                ['{:>{}}'.format(index, longest_node_id)] +
                ['{:>{}}'.format(value, spacing) for value in values]
            ))

        matrix = [line('', edge_ids)]

        for i, row in enumerate(self.incidence_matrix):
            matrix.append(line(self.nodes[i].index, row))

        return matrix

    def get_nodes_by_attr(self, attr_name, attr):
        """
        Returns nodes that have given attribute.
        """
        return [
            node for node in self.nodes if node.attr.get(attr_name) == attr
        ]

    def get_neighbour_nodes_from(self, node):
        """
        Returns neighbour nodes that can be accessed from given node.
        """
        edges_from_node = sorted([
            edge for edge in self.edges if edge.node_from == node.index
        ], key=lambda edge: edge.attr.get('weight'))
        return [
            edge.node_to for edge in edges_from_node
        ]
