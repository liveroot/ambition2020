import educative.course1.stacks_queues.ch4_queue_using_stacks_2 as queue


def main():
    print("Queue initialized with capacity = 5")
    example = queue.QueueUsingStacks_2(5, True) # suppress_printing = True

    print("------")
    print("enqueuing in queue...")
    example.enqueue(5)
    example.enqueue(6)
    example.enqueue(7)
    example.enqueue(8)
    example.enqueue(9)
    example.enqueue(2)
    example.enqueue(7)

    print()
    example.print_queue()

    print("------")
    print("peeking...")
    print(example.peek())

    print("------")
    print("dequeuing from queue...")
    example.dequeue()
    example.dequeue()

    print()
    example.print_queue()

    print("------")
    print("peeking...")
    print(example.peek())

    print("------")
    print("dequeuing from queue...")
    example.dequeue()
    example.dequeue()
    example.dequeue()
    example.dequeue()
    example.dequeue()

    print()
    example.print_queue()

    print("------")
    print("peeking...")
    print(example.peek())

    print("------")
    print("enqueuing in queue...")
    example.enqueue(21)
    example.enqueue(22)

    print()
    example.print_queue()

    print("------")
    print("peeking...")
    print(example.peek())


if __name__ == '__main__':
    main()
