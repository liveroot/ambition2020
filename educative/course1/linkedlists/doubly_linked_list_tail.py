class Node:
    def __init__(self):
        self.value = None
        self.next = None
        self.prev = None


class DoublyLinkedListTail:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def is_empty(self):
        if self.head is None and self.tail is None:
            return True

    def insert_at_head(self, data):
        new = Node()
        new.value = data
        new.prev = None

        if self.is_empty():
            new.next = None
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

    def insert_at_end(self, data):
        if self.is_empty():
            self.insert_at_head(data)
            return

        new = Node()
        new.value = data
        new.next = None
        new.prev = self.tail

        self.tail.next = new
        self.tail = new

    def insert_after(self, prev_data, data):
        if self.is_empty():
            return

        current = self.head
        while current.next is not None and current.value is not prev_data:
            current = current.next

        if current.value is not prev_data:
            print("can't insert, value not found")
            return

        new = Node()
        new.value = data
        new.prev = current

        if current.next is None:
            new.next = None
            self.tail = new
        else:
            new.next = current.next
            current.next.prev = new

        current.next = new

    def search_node(self, data):
        if self.is_empty():
            return False

        current = self.head
        while current.next is not None and current.value is not data:
            current = current.next

        if current.value is data:
            return True
        else:
            return False

    def delete_at_head(self):
        if self.is_empty():
            return

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next

    def delete_at_end(self):
        if self.is_empty():
            return

        if self.tail.prev is None:
            self.delete_at_head()
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev

    def delete_by_value(self, data):
        if self.is_empty():
            return

        if self.head.value is data:
            self.delete_at_head()
            return

        if self.tail.value is data:
            self.delete_at_end()
            return

        current = self.head
        while current.next is not None and current.value is not data:
            current = current.next

        if current.value is not data:
            print("can't delete, value not found")
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

    def print_list(self):
        if self.is_empty():
            print("list is empty")
            return

        pretty_list = self.prettify()
        print(pretty_list)

    def prettify(self):
        start_tag = "[H] None <- "
        end_tag = " -> None [T]"
        printer = ""

        printer += start_tag

        current = self.head
        while current.next is not None:
            printer += str(current.value) + " <-> "
            current = current.next

        printer += str(current.value)
        printer += end_tag

        return printer
