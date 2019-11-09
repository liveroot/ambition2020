class Node:
    def __init__(self):
        self.value = None
        self.next = None


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        if self.head is None:
            return True


def main():
    example = SinglyLinkedList()


if __name__ == "__main__":
    main()
