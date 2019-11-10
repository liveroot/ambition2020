import educative.course1.linkedlists.doubly_linked_list as dll


def main():
    example = dll.DoublyLinkedList()

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


if __name__ == '__main__':
    main()
