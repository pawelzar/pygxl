import xml.etree.ElementTree as ET

from graph import Edge, Node, Graph


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
        nodes.append(Node(node_id, node_name, node_attrs))

    return nodes


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
        edges.append(Edge(edge_id, edge_name, node_from, node_to, edge_attrs))

    return edges


def parse_graph(file):
    """
    Construct Graph object from GXL file.
    """
    tree = ET.parse(file)
    root = tree.getroot()
    nodes = parse_nodes(root)
    edges = parse_edges(root)

    return Graph(nodes, edges)


graph = parse_graph("example.gxl")
