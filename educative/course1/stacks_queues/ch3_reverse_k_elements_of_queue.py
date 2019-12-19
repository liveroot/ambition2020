import educative.course1.stacks_queues.queue as q
import educative.course1.stacks_queues.stack as s

input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
input_k = 5
expected_output_data = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]


def reverse_k_elements(queue, k):
    temp_stack = s.Stack(k)

    for i in range(k):
        temp_stack.push(queue.dequeue())

    for i in range(k):
        queue.enqueue(temp_stack.pop())

    for i in range(queue.capacity - k):
        queue.enqueue(queue.dequeue())

    return queue.prettify()


def main():
    input_queue = q.Queue(len(input_data))
    [input_queue.enqueue(x) for x in input_data]

    expected_output_queue = q.Queue(len(expected_output_data))
    [expected_output_queue.enqueue(x) for x in expected_output_data]

    print("Input: " + str(input_queue.prettify()))
    print("Expected: " + str(expected_output_queue.prettify()))
    print("Output: " + str(reverse_k_elements(input_queue, input_k)))


if __name__ == '__main__':
    main()
