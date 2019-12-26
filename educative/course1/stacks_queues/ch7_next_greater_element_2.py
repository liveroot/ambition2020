import educative.course1.stacks_queues.stack as s

input_data = [4, 6, 3, 2, 8, 1]
expected_output_data = [6, 8, 8, 8, -1, -1]


# the most optimal solution is to use a stack for storing elements yet to be processed.
# the key is to order the stack in ascending order until the next element under comparison
# is bigger than the top element on the stack.
#
# Pseudo Algo --
# for each element in input
#   if stack is empty
#       push the element to stack as stack is empty and move to the next iteration
#
#   if stack does have a node
#       if current element is smaller than top of the stack
#           push element on top of stack if element < top of stack
#
#   else
#       iterate the stack popping all elements one by one
#       and appending current element to the result array for each pop
#
#       finally after all nodes in stack are popped, push the current element
#       on top of the stack for next iteration
#
# now that all array elements are processed, we are left with
# a stack of nodes which don't have the next greater element,
# so pop them one by one and append -1 to the result array for each pop
#
# return the result array

def next_greater_element_2(input_data):
    stack = s.Stack(len(input_data), True) # suppress_printing = True
    result = []

    for x in input_data:
        if stack.is_empty():
            stack.push(x)
        else:
            if x < stack.peek():
                stack.push(x)
            else:
                while not stack.is_empty():
                    stack.pop()
                    result.append(x)

                stack.push(x)

    while not stack.is_empty():
        stack.pop()
        result.append(-1)

    return result


def main():
    print("Input: " + str(input_data))
    print("Expected: " + str(expected_output_data))
    print("Output: " + str(next_greater_element_2(input_data)))


if __name__ == '__main__':
    main()
