import networkx as nx


def stable_marriage(male_nodes, female_nodes, edges):
    nx_graph = nx.Graph()
    nx_graph.add_nodes_from(male_nodes, bipartite=0)
    nx_graph.add_nodes_from(female_nodes, bipartite=1)
    nx_graph.add_weighted_edges_from(edges, weight='weight')

    return get_edges(edges, nx.max_weight_matching(nx_graph))


def get_edges(graph_edges, connections):
    edges = []
    for connection in connections.items():
        for edge in graph_edges:
            if (edge[0], edge[1]) == connection:
                edges.append(edge)
    return edges
