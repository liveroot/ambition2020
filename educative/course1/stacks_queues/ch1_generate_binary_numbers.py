import educative.course1.stacks_queues.queue as q

input_data = 3
expected_output_data = [1, 10, 11]


def generate_binary_numbers(target_number):
    result = []
    n = target_number

    # initialize queue with capacity  n + 1, because
    # we are enqueueing 2 values for each dequeue()
    queue = q.Queue(n + 1, True) # suppress_printing = True

    # initialize queue with first value to start the conversion
    queue.enqueue(1)

    # for each entry:
    # 1. dequeue from the queue and add to result array
    # 2. append 0 and enqueue it back
    # 3. append 1 and enqueue it back
    # this process enqueues binary form of each entry to the result array
    for i in range(n):
        temp = queue.dequeue()
        result.append(temp)
        queue.enqueue(int(str(temp) + "0"))
        queue.enqueue(int(str(temp) + "1"))

    return result


def main():
    print("Input: " + str(input_data))
    print("Expected: " + str(expected_output_data))
    print("Output: " + str(generate_binary_numbers(input_data)))


if __name__ == '__main__':
    main()
