import educative.course1.linkedlists.singly_linked_list as sll


def main():
    example = sll.SinglyLinkedList()

    example.insert_at_head(5)
    example.insert_at_head(6)
    example.insert_at_head(7)
    example.insert_at_end(10)
    example.insert_at_head(8)
    example.insert_at_end(9)

    example.insert_after(6, 12)
    example.insert_after(7, 14)
    example.insert_after(10, 20)

    example.print_list()


if __name__ == '__main__':
    main()
