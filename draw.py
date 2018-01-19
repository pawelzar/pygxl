import matplotlib.pyplot as plt
import networkx as nx

from kruskal import kruskal


def draw_bipartite(graph, graph_metadata):
    pos = {node: [0, i] for i, node in enumerate(graph_metadata['nodes_female'])}
    pos.update({node: [1, i] for i, node in enumerate(graph_metadata['nodes_male'])})
    nx.draw(graph, pos, with_labels=True)
    for p in pos:  # raise text positions
        pos[p][1] += 0.25
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

    plt.show()


def draw_simple(graph, nodes):
    pos = nx.spring_layout(graph)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw(graph, pos, with_labels=True)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.show()


def draw_simple_pos(graph, nodes, pos):
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw(graph, pos, with_labels=True, node_color='c', node_size=500)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, label_pos=0.25)


def draw_kruskal(graph, pos):
    simple_graph = {
        'nodes': [node.index for node in graph.nodes],
        'edges': [
            (edge.node_from, edge.node_to, int(edge.attr.get('weight')))
            for edge in graph.edges
        ]
    }

    minimum_spanning_tree = kruskal(simple_graph)

    weight_sum = sum(edge[2] for edge in minimum_spanning_tree)
    print(minimum_spanning_tree)
    print(weight_sum)

    A = nx.Graph()
    A.add_nodes_from(simple_graph['nodes'])
    A.add_weighted_edges_from(simple_graph['edges'], weight='weight')
    draw_simple_pos(A, simple_graph['nodes'], pos)

    nodes_in_column = len(set(position[1] for position in pos.values()))
    pos_shifted = {
        node: [position[0], position[1] - nodes_in_column]
        for node, position in pos.items()
    }

    B = nx.Graph()
    B.add_nodes_from(simple_graph['nodes'])
    B.add_weighted_edges_from(minimum_spanning_tree, weight='weight')
    draw_simple_pos(B, simple_graph['nodes'], pos_shifted)

    plt.get_current_fig_manager().window.wm_geometry("+600+400")
    plt.show()
