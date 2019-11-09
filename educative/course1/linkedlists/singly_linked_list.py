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

    def insert_at_head(self, data):
        if self.is_empty():
            self.head = Node()
            self.head.value = data
            return

        new = Node()
        new.value = data
        new.next = self.head

        self.head = new


def main():
    example = SinglyLinkedList()


if __name__ == "__main__":
    main()
