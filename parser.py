from xml.etree import ElementTree

from graph import Edge, Graph, Node


class GXLParser:
    @staticmethod
    def parse_nodes(root):
        """
        Return list of Node objects extracted from GXL format.
        """
        nodes = []

        for node in root.iter('node'):
            attr = node.find('attr')
            node_id = node.attrib.get('id')
            node_name = attr.attrib.get('name')
            node_attr = [child.text for child in attr]
            nodes.append(Node(
                index=node_id,
                name=node_name,
                attr=node_attr
            ))

        return nodes

    @staticmethod
    def parse_edges(root):
        """
        Return list of Edge objects extracted from GXL format.
        """
        edges = []

        for edge in root.iter('edge'):
            attr = edge.find('attr')
            edge_id = edge.attrib.get('id')
            node_from = edge.attrib.get('from')
            node_to = edge.attrib.get('to')
            edge_name = attr.attrib.get('name')
            edge_attr = [child.text for child in attr]
            edges.append(Edge(
                index=edge_id,
                name=edge_name,
                node_from=node_from,
                node_to=node_to,
                attr=edge_attr
            ))

        return edges

    @staticmethod
    def read(input_file):
        """
        Construct Graph object from GXL file.
        """
        tree = ElementTree.parse(input_file)
        root = tree.getroot()
        nodes = GXLParser.parse_nodes(root)
        edges = GXLParser.parse_edges(root)

        return Graph(nodes, edges)


if __name__ == '__main__':
    graph = GXLParser.read('example.gxl')
    print('\n'.join(graph.incidence_matrix_str))
