import educative.course1.linkedlists.singly_linked_list as sll

incoming_input = [7, 14, 21, 14, 22]
expected_output = [7, 14, 21, 22]


# nested loop
def remove_duplicates_1(linked_list):
    current = linked_list.head

    # each outer loop element is compared with inner loop
    # one by one (brute force)
    while current:
        compare = current
        # inner loop only checks forward components
        # and deletes a node if it has the same value
        # as the outer loop pointer
        while compare.next:
            if current.value is compare.next.value:
                compare.next = compare.next.next
            else:
                compare = compare.next
        current = current.next

    return linked_list.prettify()


def main():
    input_linked_list = sll.SinglyLinkedList()
    [input_linked_list.insert_at_end(x) for x in incoming_input]

    output_linked_list = sll.SinglyLinkedList()
    [output_linked_list.insert_at_end(x) for x in expected_output]

    print("Input: " + str(input_linked_list.prettify()))
    print("Expected: " + str(output_linked_list.prettify()))
    print("Output: " + str(remove_duplicates_1(input_linked_list)))


if __name__ == '__main__':
    main()
