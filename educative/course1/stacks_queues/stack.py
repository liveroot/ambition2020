class Stack:
    def __init__(self, capacity=None):
        self.capacity = capacity
        self.top = -1
        self.elements = []

    def is_empty(self):
        if self.top is -1:
            return True
        return False

    def is_full(self):
        if self.top is (self.capacity - 1):
            return True
        return False

    def peek(self):
        if self.is_empty():
            print("nothing to show, stack empty...")
            return None

        return str(self.elements[self.top])

    def push(self, data):
        if self.is_full():
            print("can't push anymore, stack full...")
            return None

        self.elements.append(data)
        self.top += 1

    def pop(self):
        if self.is_empty():
            print("can't pop, stack empty...")
            return None

        result = self.elements[self.top]
        self.elements.remove(result)
        self.top -= 1

        return result

    def print_stack(self):
        if self.is_empty():
            print("nothing to print, stack empty...")
            return None

        pretty_list = self.prettify()
        print(pretty_list)

    def prettify(self):
        printer = ""
        for i in range(len(self.elements))[::-1]:
            printer += (str(i) + " -> " + "[ " + str(self.elements[i]) + " ]")
            if i is not 0: printer += "\n"
        return printer
