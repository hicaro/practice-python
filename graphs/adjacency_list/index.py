from graphs import Graph

if __name__ == "__main__":
    g = Graph()

    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 1)
    g.add_edge(1, 2, 1)
    g.add_edge(2, 4, 5)
    g.add_edge(2, 6, 4)
    g.add_edge(3, 2, 5)
    g.add_edge(5, 8, 2)
    g.add_edge(6, 5, 7) # uncomment to create cycle
    g.add_edge(7, 5, 3)
    g.add_edge(8, 6, 3) # uncomment to create cycle
    g.add_edge(4, 1, 2) # uncomment to create cycle

    #g.DFS()
    g.BFS()
    #g.print_debug()

    #g.count_components()