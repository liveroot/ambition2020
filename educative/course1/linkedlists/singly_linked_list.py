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

    def insert_after(self, prev, data):
        if self.is_empty():
            self.insert_at_head(data)
            return

        new = Node()
        new.value = data

        current = self.head

        while current.next is not None and current.value is not prev:
            current = current.next

        if current is not None:
            new.next = current.next
            current.next = new

    def search_node(self, data):
        if self.is_empty():
            print("list is empty")
            return False

        current = self.head
        while current.next is not None:
            if current.value is data:
                return True
            current = current.next

        return False

    def delete_at_head(self):
        if self.is_empty():
            print("list is empty")
            return

        current = self.head
        self.head = current.next

    def delete_at_end(self):
        if self.is_empty():
            print("list is empty")
            return

        current = self.head
        prev = None
        while current.next is not None:
            prev = current
            current = current.next

        prev.next = None

    def delete_by_value(self, data):
        if self.is_empty():
            print("list is empty")
            return

        current = self.head
        prev = None

        if current.value is data:
            self.delete_at_head()
            return

        while current.next is not None:
            if current.value is data:
                prev.next = current.next
                return
            prev = current
            current = current.next

        print("value not found")

    def print_list(self):
        if self.is_empty():
            print("list is empty")
            return

        current = self.head
        while current.next is not None:
            print(current.value)
            current = current.next

        print(current.value)
