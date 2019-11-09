import educative.course1.linkedlists.singly_linked_list as sll


def main():
    example = sll.SinglyLinkedList()

    # inserting at head
    example.insert_at_head(5)
    example.insert_at_head(6)
    example.insert_at_head(7)
    example.insert_at_head(8)

    # inserting at end
    example.insert_at_end(10)
    example.insert_at_end(9)

    # inserting after a node
    example.insert_after(6, 12)
    example.insert_after(7, 14)
    example.insert_after(10, 20)

    # printing list
    example.print_list()

    # deleting at head
    example.delete_at_head()
    print("after deleting at head")
    example.print_list()

    # searching in linked list
    if example.search_node(7):
        print("node is found")
    else:
        print("node not found")


if __name__ == '__main__':
    main()
