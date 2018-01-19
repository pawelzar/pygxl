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
            attributes = node.findall('attr')
            node_id = node.get('id')
            #import ipdb;ipdb.set_trace()
            node_attr = {
                attr.get('name'): attr[0].text for attr in attributes
            }
            nodes.append(Node(
                index=node_id,
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
            attributes = edge.findall('attr')
            edge_id = edge.get('id')
            node_from = edge.get('from')
            node_to = edge.get('to')
            edge_attr = {
                attr.get('name'): attr[0].text for attr in attributes
            }
            edges.append(Edge(
                index=edge_id,
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
