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
            attributes = {
                attr.get('name'): attr[0].text for attr in node.findall('attr')
            }
            nodes.append(Node(
                index=node.get('id'),
                attr=attributes,
            ))

        return nodes

    @staticmethod
    def parse_edges(root):
        """
        Return list of Edge objects extracted from GXL format.
        """
        edges = []

        for edge in root.iter('edge'):
            attributes = {
                attr.get('name'): attr[0].text for attr in edge.findall('attr')
            }
            edges.append(Edge(
                index=edge.get('id'),
                node_from=edge.get('from'),
                node_to=edge.get('to'),
                attr=attributes,
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
