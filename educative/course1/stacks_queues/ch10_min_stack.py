import educative.course1.stacks_queues.stack as s


# Min Stack implementation returns the minimum element
# of a stack in O(1), instead of O(n) which will be the
# case if we searched for the minimum value every time
#
# This is achieved by keeping track of the minimum value
# is a separate stack in parallel to the main stack
# ---------
# Solution:
# ---------
# push() ->
# 1. push data to main_stack
# 2. if min stack is empty:
#       push the data to min stack and return
# 3. if data <= min_stack.top
#       push the data to min stack and return
# pop() ->
# 1. if min_stack is not empty:
#       if min_stack.peek() == main_stack.peek()
#           min_stack.pop()
# 2. return main_stack.pop()
# min() ->
# 1. if min_stack is not empty:
#       return min_stack.peek() -> (top of min_stack)
# ---------
class MinStack():
    def __init__(self, capacity=None, suppress_printing=False):
        self.suppress_printing = suppress_printing
        self.capacity = capacity
        self.stack = s.Stack(capacity, suppress_printing)
        self.min_stack = s.Stack(capacity, suppress_printing)

    def is_full(self):
        if self.stack.is_full():
            return True
        return False

    def is_empty(self):
        if self.stack.is_empty():
            return True
        return False

    def push(self, data):
        if self.is_full():
            print("can't push anymore, stack full...")
            return None

        self.stack.push(data)
        if not self.suppress_printing: print("pushed data = " + str(data))

        if self.min_stack.is_empty():
            self.min_stack.push(data)
            if not self.suppress_printing: print("pushed data to min stack = " + str(data))
            return None

        if data <= self.min_stack.peek():
            self.min_stack.push(data)
            if not self.suppress_printing: print("pushed data to min stack = " + str(data))

        return None

    def pop(self):
        if self.is_empty():
            print("can't pop, stack empty...")
            return None

        if not self.min_stack.is_empty():
            if self.min_stack.peek() is self.stack.peek():
                min_pop = self.min_stack.pop()
                if not self.suppress_printing: print("popped data from min stack= " + str(min_pop))

        popped = self.stack.pop()
        if not self.suppress_printing: print("popped data (main stack) = " + str(popped))

        return popped

    def peek(self):
        if self.stack.is_empty():
            print("nothing at top, stack empty...")
            return None
        return self.stack.peek()

    def min(self):
        if self.stack.is_empty():
            print("no min exists, stack empty...")

        return self.min_stack.peek()

    def print_stack(self):
        pretty_list = self.prettify()
        print(pretty_list)

        return None

    def print_min_stack(self):
        pretty_list = self.prettify_min()
        print(pretty_list)

        return None

    def prettify(self):
        printer = "main:\n"
        for i in range(self.capacity)[::-1]:
            printer += str(self.capacity - i -1) + " -> [  " + str(self.stack.elements[i]) + "  ]"
            if i is not self.capacity: printer += "\n"

        return printer

    def prettify_min(self):
        printer = "min:\n"
        for i in range(self.capacity)[::-1]:
            printer += str(self.capacity - i - 1) + " -> [  " + str(self.min_stack.elements[i]) + "  ]"
            if i is not self.capacity: printer += "\n"

        return printer
