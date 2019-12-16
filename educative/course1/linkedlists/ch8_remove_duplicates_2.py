import educative.course1.linkedlists.singly_linked_list as sll

incoming_input = [7, 14, 21, 14, 22]
expected_output = [7, 14, 21, 22]


def remove_duplicates_2(linked_list):
    prev = linked_list.head
    current = linked_list.head
    value_set = set()

    while current:
        if current.value not in value_set:
            value_set.add(current.value)
            prev = current
            current = current.next
        else:
            prev.next = current.next
            current = current.next

    return linked_list.prettify()


def main():
    input_linked_list = sll.SinglyLinkedList()
    [input_linked_list.insert_at_end(x) for x in incoming_input]

    output_linked_list = sll.SinglyLinkedList()
    [output_linked_list.insert_at_end(x) for x in expected_output]

    print("Input: " + str(input_linked_list.prettify()))
    print("Expected: " + str(output_linked_list.prettify()))
    print("Output: " + str(remove_duplicates_2(input_linked_list)))


if __name__ == '__main__':
    main()
