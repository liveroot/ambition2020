import educative.course1.stacks_queues.stack as s


# Implementation uses 2 stacks, one for storing the queue elements,
# and 2nd as a buffer to be used at the time of dequeue
# 1. Enqueue simply pushes the value on top of stack 1
# 2. Dequeue checks if stack 1 is empty and returns False if no elements
# 3. Then stack 1 is emptied into stack 2
# 4. This operation brings the first value in the queue to the top of stack 2
# 5. Now it is popped and saved for returning to the caller
# 6. Finally stack 2 is emptied back into stack 1 and the queue returns to normal.
# 7. Finally, result is returned to the caller
class QueueUsingStacks_1:
    def __init__(self, capacity=None):
        self.capacity = capacity
        self.stack1 = s.Stack(self.capacity)
        self.stack2 = s.Stack(self.capacity)

    def is_empty(self):
        if self.stack1.is_empty():
            return True
        return False

    def is_full(self):
        if self.stack1.is_full():
            return True
        return False

    def peek(self):
        if self.is_empty():
            print("nothing to show, queue empty...")
            return None

        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())

        result = self.stack2.peek()

        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())

        return result

    def enqueue(self, data):
        if self.is_full():
            print("can't enqueue anymore, queue full...")
            return False

        self.stack1.push(data)
        print("enqueued data = " + str(data))

        return True

    def dequeue(self):
        if self.is_empty():
            print("can't dequeue, queue empty...")
            return None

        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())

        result = self.stack2.pop()

        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())

        print("dequeued data = " + str(result))
        return result

    def print_queue(self):
        pretty_queue = self.prettify()
        print(pretty_queue)

    def prettify(self):
        printer = "Queue -> F [ "
        for x in self.stack1.elements:
            printer += str(x) + " "
        printer += "] B"

        return printer
