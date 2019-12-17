import educative.course1.linkedlists.singly_linked_list as sll

incoming_input = [22, 18, 60, 78, 47, 39, 99]
n = 3
expected_output = 47


def return_nth_from_end(linked_list, n):
    # nth from end means size - n + 1 from beginning,
    # so calculate size
    size = 0
    current = linked_list.head
    while current:
        size += 1
        current = current.next

    # m = size - n + 1
    m = size - n + 1

    count = 0
    current = linked_list.head
    while current:
        count += 1
        if count is m:
            return current.value
        current = current.next

    return None


def main():
    input_linked_list = sll.SinglyLinkedList()
    [input_linked_list.insert_at_end(x) for x in incoming_input]

    print("Input: " + str(input_linked_list.prettify()) + ", n = " + str(n))
    print("Expected: " + str(expected_output))
    print("Output: " + str(return_nth_from_end(input_linked_list, n)))


if __name__ == '__main__':
    main()
