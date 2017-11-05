from unittest import TestCase

from graph import Edge, Graph, Node


class GraphTestCase(TestCase):
    def setUp(self):
        self.nodes = [
            Node('v1'),
            Node('v2'),
            Node('v3'),
            Node('v4'),
        ]
        self.edges = [
            Edge('edge 1', node_from='v1', node_to='v2'),
            Edge('edge 2', node_from='v1', node_to='v3'),
            Edge('edge 3', node_from='v3', node_to='v2'),
            Edge('edge 4', node_from='v3', node_to='v4'),
            Edge('edge 5', node_from='v4', node_to='v3'),
        ]
        self.graph = Graph(self.nodes, self.edges)

    def test_incidence_matrix(self):
        expected_matrix = [
            [1,  1,  0,  0,  0],
            [-1, 0, -1,  0,  0],
            [0, -1,  1,  1, -1],
            [0,  0,  0, -1,  1],
        ]
        self.assertEqual(self.graph.incidence_matrix, expected_matrix)

    def test_incidence_matrix_str(self):
        expected_matrix = [
            '   edge 1 edge 2 edge 3 edge 4 edge 5',
            'v1      1      1      0      0      0',
            'v2     -1      0     -1      0      0',
            'v3      0     -1      1      1     -1',
            'v4      0      0      0     -1      1',
        ]
        self.assertEqual(self.graph.incidence_matrix_str, expected_matrix)
