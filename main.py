from draw import draw_kruskal, draw_stable_marriage
from gxlparser import GXLParser


if __name__ == '__main__':

    # STABLE MARRIAGE PROBLEM

    graph = GXLParser.read('data/marriage.gxl')
    draw_stable_marriage(graph)

    # WIKIPEDIA MINIMUM SPANNING TREE EXAMPLES

    graph = GXLParser.read('data/kruskal_simple.gxl')
    node_positions = {
        'A': (0, 1),
        'B': (1, 1),
        'C': (2, 1),
        'D': (0, 0),
        'E': (1, 0),
        'F': (2, 0),
    }
    draw_kruskal(graph, node_positions)

    graph = GXLParser.read('data/kruskal_one.gxl')
    draw_kruskal(graph, node_positions)

    # MORE COMPLEX MINIMUM SPANNING TREE EXAMPLE

    graph = GXLParser.read('data/kruskal.gxl')
    node_positions = {
        '0': (0, 2),
        '1': (1, 2),
        '2': (2, 2),
        '3': (0, 1),
        '4': (1, 1),
        '5': (0, 0),
        '6': (1, 0),
        '7': (2, 0),
    }
    draw_kruskal(graph, node_positions)
