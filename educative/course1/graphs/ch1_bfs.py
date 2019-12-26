import educative.course1.stacks_queues.queue as q
import educative.course1.graphs.graph as g

input_num_vertices = 5
input_edges = {0: [1, 2], 1: [3, 4]}
expected_output = "01234"


# this code implements Breadth First Traversal in a graph. Each element in the graph's adjacency list
# represents a list of nodes directly connected to the current element. Each of these lists represent
# levels in the graph. We traverse all nodes in a certain level, before moving to the next one.
# --------------
# For traversal:
# --------------
# 1. We first enqueue the root node in a queue and mark it visited.
# 2. Now we get the list of adjacent nodes from the root node and enqueue all adjacent nodes in the list
#    to the queue.
# 3. As we are adding the adjacent nodes to the queue, we mark them as visited.
# 4. Simultaneously, we dequeue the nodes from the queue and append the node's value to the result
# --------------
def bfs_traversal(graph, root):
    result = ""
    visited = [False] * graph.num_vertices
    queue = q.Queue(graph.num_vertices, True) # supress_printing = True

    queue.enqueue(root)
    visited[root] = True

    while not queue.is_empty():
        g_node = queue.dequeue()
        result += str(g_node)

        dll = graph.adjacency_list[g_node]
        if dll is not None:
            current = dll.head
            while current:
                if not visited[current.value]:
                    queue.enqueue(current.value)
                    visited[current.value] = True
                current = current.next

    return result


def main():
    # create a graph from input data
    graph = g.Graph(input_num_vertices, True) # suppress_printing = True
    for x in input_edges.keys():
        for y in input_edges[x]:
            graph.add_edge(x, y)

    # set a starting point for traversal
    root = 0

    print("Input:")
    print("Graph in Adjacency List Representation:")
    print(str(graph.prettify()))

    print("Expected: " + str(expected_output))
    print("Output: " + str(bfs_traversal(graph, root)))


if __name__ == '__main__':
    main()
