import networkx as nx

def stable_marriage(graph):
    A = nx.Graph()
    A.add_nodes_from(graph['males'], bipartite=0)
    A.add_nodes_from(graph['females'], bipartite=1)
    A.add_weighted_edges_from(graph['edges'], weight='weight')

    return get_edges(graph, nx.max_weight_matching(A))


def get_edges(graph, connections):
    edges = []
    for connection in connections.items():
        for edge in graph['edges']:
            if (edge[0], edge[1]) == connection:
                edges.append(edge)
    return edges
