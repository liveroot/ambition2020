import educative.course1.stacks_queues.stack as s

input_data = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]
input_num_people = 4 # num rows in the input array
expected_output_data = 2


# 1. input_data[row][col] = 1 means row knows column
# 2. input_data[row][col] = 0 means row does not know col
# 3. a celebrity does not know anyone, but everyone knows a celebrity.
# 4. assume there is at max a single celebrity at the party
#
# row index represents a person identifier eg. row 1 represents the guest no. 2 at the party,
# columns represent if the guest knows another guest whose row index is same as column index
#
# meaning in above example:
# - guest no. 1 knows guest no. 2 and guest no. 3, but not guest no. 4
# - guest no. 2 knows guest no. 1, guest no. 3 and guest no. 4
# - guest no. 4 only knows guest no. 2 and guest no. 3, but not guest no. 1
# - guest no. 3 however does not know anybody.
# --> this means guest no. 3 is a celebrity as everyone else knows guest no. 3,
#     but guest no. 3 does not know anyone
#
# Solution:
# 1. push all row indices (guest ids) in a stack
# 2. pop guest ids from stack until stack is empty, 2 at a time
# 3. if party[x][y] 1, means guest x knows guest y
#       push next guest y to stack and discard x
#    else:
#       push guest x back to stack, ignoring y (compare x with y+1 in the next iteration)
# 4. Finally the stack only contains 1 guest, it means everyone knows that guest
# 5. Now assume that guest is a celebrity and check if the guest knows anyone else at the party.
# 6. If the guest knows anyone:
#       means they are not a celebrity and return -1 (no celebrity)
#    else:
#        guest is a celebrity and return guest id
def find_celebrity(party_data, num_people):
    stack = s.Stack(num_people)
    celebrity = -1

    for i in range(num_people):
        stack.push(i)

    while not stack.is_empty():
        x = stack.pop()

        # check if stack empty before popping second guest id
        if stack.is_empty():
            # if stack empty, previously popped guest id is the last id
            # and therefore we assume everyone knows them.
            celebrity = x
            break

        y = stack.pop()

        if party_data[x][y] is 1:
            stack.push(y)
        else:
            stack.push(x)

    for i in range(num_people):
        if celebrity is not i:
            if (party_data[celebrity][i] is 1) or (not party_data[i][celebrity] is 1):
                return -1

    return celebrity


def main():
    print("Input: " + str(input_data))
    print("Expected: " + str(expected_output_data))
    print("Output: " + str(find_celebrity(input_data, input_num_people)))


if __name__ == '__main__':
    main()
