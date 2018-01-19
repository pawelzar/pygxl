from draw import draw_kruskal
from parser import GXLParser


if __name__ == '__main__':

    # WIKIPEDIA MINIMUM SPANNING TREE EXAMPLES

    graph = GXLParser.read('data/kruskal_simple.gxl')
    pos = {
        'A': [0, 1],
        'B': [1, 1],
        'C': [2, 1],
        'D': [0, 0],
        'E': [1, 0],
        'F': [2, 0],
    }
    draw_kruskal(graph, pos)

    graph = GXLParser.read('data/kruskal_one.gxl')
    draw_kruskal(graph, pos)


    # MORE COMPLEX MINIMUM SPANNING TREE EXAMPLE

    graph = GXLParser.read('data/kruskal.gxl')
    pos = {
        '0': [0, 2],
        '1': [1, 2],
        '2': [2, 2],
        '3': [0, 1],
        '4': [1, 1],
        '5': [0, 0],
        '6': [1, 0],
        '7': [2, 0],
    }
    draw_kruskal(graph, pos)
