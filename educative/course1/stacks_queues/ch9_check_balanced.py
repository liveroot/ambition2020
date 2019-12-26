import educative.course1.stacks_queues.stack as s

input_string = "{[({})]}"
expected_output = True


# we can check if the parentheses are balanced by pushing all opening parentheses on to a stack
# and then popping elements one by one, comparing next character with the popped element in a loop
# if the current character is not the closing parentheses of the popped element, it means the string is not balanced, so return False
def check_balanced(expression):
    input_chars = list(expression)
    stack = s.Stack(len(input_chars), True) # suppress_printing = True

    for char in input_chars:
        if char is "{" or char is "[" or char is "(":
            stack.push(char)
        else:
            if stack.is_empty():
                # if the string is unbalanced, number of opening parentheses do not match with the
                # closing parentheses, this will lead to stack running empty before the whole string
                # has been processed, so return False
                return False
            if char is "}" and stack.pop() is not "{":
                return False
            if char is "]" and stack.pop() is not "[":
                return False
            if char is ")" and stack.pop() is not "(":
                return False

    if not stack.is_empty():
        return False

    return True


def main():
    print("Input: " + str(input_string))
    print("Expected: " + str(expected_output))
    print("Output: " + str(check_balanced(input_string)))


if __name__ == '__main__':
    main()
