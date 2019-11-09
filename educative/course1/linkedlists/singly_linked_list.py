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

    def insert_at_end(self, data):
        if self.is_empty():
            self.insert_at_head(data)
            return

        new = Node()
        new.value = data
        new.next = None

        last = self.head
        while last.next is not None:
            last = last.next

        last.next = new


def main():
    example = SinglyLinkedList()


if __name__ == "__main__":
    main()
