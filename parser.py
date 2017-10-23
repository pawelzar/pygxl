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
            attrs = node.find('attr')
            node_id = node.attrib.get('id')
            node_name = attrs.attrib.get('name')
            node_attrs = [child.text for child in attrs]
            nodes.append(Node(
                index=node_id,
                name=node_name,
                attrs=node_attrs
            ))

        return nodes

    @staticmethod
    def parse_edges(root):
        """
        Return list of Edge objects extracted from GXL format.
        """
        edges = []

        for edge in root.iter('edge'):
            attrs = edge.find('attr')
            edge_id = edge.attrib.get('id')
            node_from = edge.attrib.get('from')
            node_to = edge.attrib.get('to')
            edge_name = attrs.attrib.get('name')
            edge_attrs = [child.text for child in attrs]
            edges.append(Edge(
                index=edge_id,
                name=edge_name,
                node_from=node_from,
                node_to=node_to,
                attrs=edge_attrs
            ))

        return edges

    @staticmethod
    def read(file):
        """
        Construct Graph object from GXL file.
        """
        tree = ElementTree.parse(file)
        root = tree.getroot()
        nodes = GXLParser.parse_nodes(root)
        edges = GXLParser.parse_edges(root)

        return Graph(nodes, edges)


if __name__ == '__main__':
    graph = GXLParser.read('example.gxl')
    graph.draw_incidence_matrix()
