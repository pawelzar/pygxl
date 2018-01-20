import matplotlib.pyplot as plt
import networkx as nx

from algorithms.kruskal import kruskal
from algorithms.stable_marriage import stable_marriage


def shift_position(pos):
    nodes_in_column = len(set(position[1] for position in pos.values()))
    return {
        node: [position[0], position[1] - nodes_in_column]
        for node, position in pos.items()
    }

def draw_simple(graph, nodes):
    pos = nx.spring_layout(graph)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw(graph, pos, with_labels=True)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.show()


def draw_simple_pos(graph, pos):
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw(graph, pos, with_labels=True, node_color='c', node_size=500)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, label_pos=0.25)


def draw_kruskal(graph, pos):
    simple_graph = {
        'nodes': [node.index for node in graph.nodes],
        'edges': [
            (edge.node_from, edge.node_to, int(edge.attr.get('weight')))
            for edge in graph.edges
        ],
    }

    minimum_spanning_tree = kruskal(simple_graph)

    weight_sum = sum(edge[2] for edge in minimum_spanning_tree)
    for edge in sorted(minimum_spanning_tree):
        print(edge)
    print('Total weight: {}'.format(weight_sum))

    A = nx.Graph()
    A.add_nodes_from(simple_graph['nodes'])
    A.add_weighted_edges_from(simple_graph['edges'], weight='weight')
    draw_simple_pos(A, pos)

    pos_shifted = shift_position(pos)

    B = nx.Graph()
    B.add_nodes_from(simple_graph['nodes'])
    B.add_weighted_edges_from(minimum_spanning_tree, weight='weight')
    draw_simple_pos(B, pos_shifted)

    plt.get_current_fig_manager().window.wm_geometry("+400+100")
    plt.show()


def draw_stable_marriage(graph):
    simple_graph = {
        'males': [n.index for n in graph.get_nodes_by_attr('gender', 'male')],
        'females': [n.index for n in graph.get_nodes_by_attr('gender', 'female')],
        'edges': [
            (edge.node_from, edge.node_to, int(edge.attr.get('weight')))
            for edge in graph.edges
        ],
    }
    pos = {node: [i, 0] for i, node in enumerate(simple_graph['males'])}
    pos.update({node: [i, 1] for i, node in enumerate(simple_graph['females'])})

    marriage_edges = stable_marriage(simple_graph)
    weight_sum = 0
    for (male, female, weight) in marriage_edges:
        print('{} & {}'.format(male, female))
        weight_sum += weight
    print('Total weight: {}'.format(weight_sum))

    A = nx.Graph()
    A.add_nodes_from(simple_graph['males'], bipartite=0)
    A.add_nodes_from(simple_graph['females'], bipartite=1)
    A.add_weighted_edges_from(simple_graph['edges'], weight='weight')
    draw_simple_pos(A, pos)

    pos_shifted = shift_position(pos)

    B = nx.Graph()
    B.add_nodes_from(simple_graph['males'], bipartite=0)
    B.add_nodes_from(simple_graph['females'], bipartite=1)
    B.add_weighted_edges_from(marriage_edges, weight='weight')
    draw_simple_pos(B, pos_shifted)

    plt.get_current_fig_manager().window.wm_geometry("+400+100")
    plt.show()
