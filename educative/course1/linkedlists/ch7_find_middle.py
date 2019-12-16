import educative.course1.linkedlists.singly_linked_list as sll

incoming_input = [7, 14, 10, 21]
expected_output = 14


# current pointer jumps twice and mid only jumps once,
# so when loop terminates, middle value is found
def find_middle(linked_list):
    mid = linked_list.head
    current = linked_list.head

    while mid and current and current.next:
        current = current.next.next
        if current:
            mid = mid.next

    return mid.value


def main():
    input_linked_list = sll.SinglyLinkedList()
    [input_linked_list.insert_at_end(x) for x in incoming_input]

    print("Input: " + str(input_linked_list.prettify()))
    print("Expected: " + str(expected_output))
    print("Output: " + str(find_middle(input_linked_list)))


if __name__ == '__main__':
    main()
