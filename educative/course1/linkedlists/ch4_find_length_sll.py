import educative.course1.linkedlists.singly_linked_list as sll

elements = [0, 1, 2, 3, 4]
result = 5


def find_length(linked_list):
    count = 0

    current = linked_list.head
    while current:
        count += 1
        current = current.next

    return count


def main():
    linked_list = sll.SinglyLinkedList()
    [linked_list.insert_at_end(x) for x in elements]
    pretty_list = linked_list.prettify()

    print("Input: " + str(pretty_list))
    print("Expected: " + str(result))
    print("Output: " + str(find_length(linked_list)))


if __name__ == '__main__':
    main()
