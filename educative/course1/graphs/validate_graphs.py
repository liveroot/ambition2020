import educative.course1.graphs.graph as g


def main():
    print("instantiating a graph with 5 vertices...")
    example = g.Graph(5)

    print()
    print("adding edges between vertices...")
    example.add_edge(0, 1)
    example.add_edge(0, 2)
    example.add_edge(1, 3)
    example.add_edge(1, 4)
    example.add_edge(2, 1)
    example.add_edge(2, 4)
    example.add_edge(2, 0)
    example.add_edge(3, 1)
    example.add_edge(4, 0)

    print()
    print("adding edge on vertex back to itself...")
    example.add_edge(1, 1)

    print()
    print("adding edge for a non-existent source vertex...")
    example.add_edge(5, 0)

    print()
    print("adding edge for a non-existent destination vertex...")
    example.add_edge(0, 5)

    print()
    print("printing graph adjacency list...")
    example.print_graph()


if __name__ == '__main__':
    main()
