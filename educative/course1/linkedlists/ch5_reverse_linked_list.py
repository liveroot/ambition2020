import educative.course1.linkedlists.singly_linked_list as sll

incoming_elements = [10, 9, 4, 4, 6]
expected_elements = [6, 4, 4, 9, 10]


def reverse_linked_list(linked_list):
    prev_node = None
    current = linked_list.head
    next_node = None

    while current:
        next_node = current.next
        current.next = prev_node
        prev_node = current
        current = next_node

    linked_list.head = prev_node

    return linked_list.prettify()


def main():
    input_linked_list = sll.SinglyLinkedList()
    [input_linked_list.insert_at_end(x) for x in incoming_elements]

    expected_linked_list = sll.SinglyLinkedList()
    [expected_linked_list.insert_at_end(x) for x in expected_elements]

    print("Input: " + str(input_linked_list.prettify()))
    print("Expected: " + str(expected_linked_list.prettify()))
    print("Output: " + str(reverse_linked_list(input_linked_list)))


if __name__ == '__main__':
    main()
