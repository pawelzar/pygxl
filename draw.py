import matplotlib.pyplot as plt
import networkx as nx

from algorithms.kruskal import kruskal
from algorithms.stable_marriage import stable_marriage


def shift_position(node_positions):
    nodes_in_column = len(set(y for x, y in node_positions.values()))
    return {
        node: (x, y - nodes_in_column)
        for node, (x, y) in node_positions.items()
    }


def draw_graph(graph, node_positions=None):
    if not node_positions:
        node_positions = nx.spring_layout(graph)

    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw(
        graph, node_positions, with_labels=True, node_color='c', node_size=500
    )
    nx.draw_networkx_edge_labels(
        graph, node_positions, edge_labels=labels, label_pos=0.25
    )


def draw_kruskal(graph, node_positions):
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

    initial_graph = nx.Graph()
    initial_graph.add_nodes_from(simple_graph['nodes'])
    initial_graph.add_weighted_edges_from(simple_graph['edges'])
    draw_graph(initial_graph, node_positions)

    solution_graph = nx.Graph()
    solution_graph.add_nodes_from(simple_graph['nodes'])
    solution_graph.add_weighted_edges_from(minimum_spanning_tree)
    draw_graph(solution_graph, shift_position(node_positions))

    plt.get_current_fig_manager().window.wm_geometry('+400+100')
    plt.show()


def draw_stable_marriage(graph):
    simple_graph = {
        'male_nodes': [
            node.index for node in graph.get_nodes_by_attr('gender', 'male')
        ],
        'female_nodes': [
            node.index for node in graph.get_nodes_by_attr('gender', 'female')
        ],
        'edges': [
            (edge.node_from, edge.node_to, int(edge.attr.get('weight')))
            for edge in graph.edges
        ],
    }

    node_positions = {
        **{n: (i, 0) for i, n in enumerate(simple_graph['male_nodes'])},
        **{n: (i, 1) for i, n in enumerate(simple_graph['female_nodes'])},
    }

    marriage_edges = stable_marriage(**simple_graph)
    weight_sum = 0
    for (male, female, weight) in marriage_edges:
        print('{} & {}'.format(male, female))
        weight_sum += weight
    print('Total weight: {}'.format(weight_sum))

    initial_graph = nx.Graph()
    initial_graph.add_nodes_from(simple_graph['male_nodes'], bipartite=0)
    initial_graph.add_nodes_from(simple_graph['female_nodes'], bipartite=1)
    initial_graph.add_weighted_edges_from(simple_graph['edges'])
    draw_graph(initial_graph, node_positions)

    solution_graph = nx.Graph()
    solution_graph.add_nodes_from(simple_graph['male_nodes'], bipartite=0)
    solution_graph.add_nodes_from(simple_graph['female_nodes'], bipartite=1)
    solution_graph.add_weighted_edges_from(marriage_edges)
    draw_graph(solution_graph, shift_position(node_positions))

    plt.get_current_fig_manager().window.wm_geometry('+400+100')
    plt.show()
