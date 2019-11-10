import educative.course1.linkedlists.singly_linked_list as sll


def main():
    example = sll.SinglyLinkedList()

    # inserting at head
    print("inserting at head...")
    example.insert_at_head(5)
    example.insert_at_head(6)
    example.insert_at_head(7)
    example.insert_at_head(8)

    # inserting at end
    print("inserting at end...")
    example.insert_at_end(10)
    example.insert_at_end(9)

    # inserting after a node
    print("inserting after...")
    example.insert_after(6, 12)
    example.insert_after(7, 14)
    example.insert_after(10, 20)

    # printing list
    example.print_list()

    # deleting at head
    print("deleting at head...")
    example.delete_at_head()
    example.print_list()

    # deleting by value
    print("deleting by value...")
    example.delete_by_value(12)
    example.print_list()

    # deleting by value
    print("deleting at end...")
    example.delete_at_end()
    example.print_list()

    # searching in linked list
    print("searching node...")
    if example.search_node(7):
        print("node is found")
    else:
        print("node not found")


if __name__ == '__main__':
    main()
