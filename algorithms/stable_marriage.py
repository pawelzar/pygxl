import networkx as nx


def stable_marriage(graph):
    nx_graph = nx.Graph()
    nx_graph.add_nodes_from(graph['males'], bipartite=0)
    nx_graph.add_nodes_from(graph['females'], bipartite=1)
    nx_graph.add_weighted_edges_from(graph['edges'], weight='weight')

    return get_edges(graph, nx.max_weight_matching(nx_graph))


def get_edges(graph, connections):
    edges = []
    for connection in connections.items():
        for edge in graph['edges']:
            if (edge[0], edge[1]) == connection:
                edges.append(edge)
    return edges
