import educative.course1.linkedlists.singly_linked_list as sll

incoming_input_1 = [15, 22, 8]
incoming_input_2 = [7, 14, 22]
expected_output_union = [15, 22, 8, 7, 14]
expected_output_intersection = [22]


# the best way to perform union of two linked lists is to connect
# the tail of list1 and head of list2, and them remove any duplicate
# items from the merged list.
def union(linked_list_1, linked_list_2):
    current = linked_list_1.head
    while current.next:
        current = current.next

    # linking linked_list_1's tail to linked_list_2's head
    current.next = linked_list_2.head
    # removing duplicates from the combined list
    h_remove_duplicates(linked_list_1)

    return linked_list_1.prettify()


# The best way to obtain an intersection list of list1 and list2
# is to check each element of list1 against list2 and copy common nodes
# to a new intersection list.
def intersection(linked_list_1, linked_list_2):
    output_linked_list = sll.SinglyLinkedList()
    current = linked_list_1.head
    while current:
        # checking if linked_list_2 contains an element with current node's value.
        # if yes, insert in the output linked list
        if h_contains(linked_list_2, current.value):
            output_linked_list.insert_at_end(current.value)
        current = current.next

    return output_linked_list.prettify()


# Helper function to check value of a node against nodes in a linked list.
# Returns true if element found, else returns false
def h_contains(linked_list, data):
    current = linked_list.head

    while current:
        if current.value is data:
            return True
        current = current.next

    return False


# Helper function to remove duplicates from a list.
# Returns a linked list with only unique elements.
def h_remove_duplicates(linked_list):
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
    return linked_list


def main():
    # import input arrays as input linked lists for union
    input_linked_list_1_union = sll.SinglyLinkedList()
    [input_linked_list_1_union.insert_at_end(x) for x in incoming_input_1]
    input_linked_list_2_union = sll.SinglyLinkedList()
    [input_linked_list_2_union.insert_at_end(x) for x in incoming_input_2]

    # import input arrays as input linked lists for intersection
    input_linked_list_1_intersection = sll.SinglyLinkedList()
    [input_linked_list_1_intersection.insert_at_end(x) for x in incoming_input_1]
    input_linked_list_2_intersection = sll.SinglyLinkedList()
    [input_linked_list_2_intersection.insert_at_end(x) for x in incoming_input_2]

    # import expected output arrays as output linked lists for union
    output_linked_list_union = sll.SinglyLinkedList()
    [output_linked_list_union.insert_at_end(x) for x in expected_output_union]
    output_linked_list_intersection = sll.SinglyLinkedList()
    [output_linked_list_intersection.insert_at_end(x) for x in expected_output_intersection]

    print("Input 1: " + str(input_linked_list_1_union.prettify()))
    print("Input 2: " + str(input_linked_list_2_union.prettify()))

    print("Expected Union: " + str(output_linked_list_union.prettify()))
    print("Output Union: " + str(union(input_linked_list_1_union, input_linked_list_2_union)))

    print("Expected Intersection: " + str(output_linked_list_intersection.prettify()))
    print("Output Intersection: " + str(intersection(input_linked_list_1_intersection, input_linked_list_2_intersection)))


if __name__ == '__main__':
    main()
