import educative.course1.linkedlists.doubly_linked_list_tail as dll_t


# implemented as adjacency list
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_list = [None] * self.num_vertices

        for i in range(self.num_vertices):
            self.adjacency_list[i] = dll_t.DoublyLinkedListTail()

    def add_edge(self, source, destination):
        if destination > self.num_vertices - 1 and source > self.num_vertices - 1:
            print("can't add edge, source/destination vertex do not exist...")
        elif source > self.num_vertices - 1:
            print("can't add edge, source vertex does not exist...")
        elif destination > self.num_vertices - 1:
            print("can't add edge, destination vertex does not exist...")
        else:
            # for directed graphs ----------------------------------
            self.adjacency_list[source].insert_at_end(destination)
            print("added edge: " + str(source) + " -> " + str(destination))
            # ------------------------------------------------------

            # for undirected graphs --------------------------------
            # self.adjacency_list[destination].insert_at_end(source)
            # print("added edge: " + str(source) + " <- " + str(destination))
            # ------------------------------------------------------

        return None

    def print_graph(self):
        print(self.prettify())

        return None

    def prettify(self):
        printer = ""
        for i in range(self.num_vertices):
            printer += "| " + str(i) + " | --> " + self.adjacency_list[i].prettify() + "\n"

        return printer
