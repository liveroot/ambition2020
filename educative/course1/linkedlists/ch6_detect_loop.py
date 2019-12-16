import educative.course1.linkedlists.singly_linked_list as sll

incoming_input = [7, 14, 21]
expected_output = True


# using floyd's cycle detection algorithm
def detect_loop(linked_list):
    slow = linked_list.head
    fast = linked_list.head

    while slow and fast:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False


def main():
    input_linked_list = sll.SinglyLinkedList()
    [input_linked_list.insert_at_end(x) for x in incoming_input]

    # Adding Loop
    input_linked_list.head.next.next.next = input_linked_list.head

    # can't print input_linked_list after adding a loop, so creating
    # a textual representation of a looped input_linked_list to print as Input
    printer = "[H] "
    for i in range(3):
        for x in incoming_input[0:3]:
            printer += str(x) + ' -> '

    printer += "..."

    print("Input: " + str(printer))
    print("Expected: " + str(expected_output))
    print("Output: " + str(detect_loop(input_linked_list)))


if __name__ == '__main__':
    main()
