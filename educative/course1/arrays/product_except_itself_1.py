array = [1,2,3,4]
result = [24,12,8,6]


# MAY NOT WORK FOR ALL INPUTS
def product_except_itself_1(arr):
    output = []

    # set temp = 1 as a starter
    temp = 1

    # iterate loop twice and multiple inner loop values except itself
    for x in arr:
        for y in arr:
            if x != y:
                temp = temp * y

        output.append(temp)

        # reset temp = 1
        temp = 1;

    return output


print("Input: " + str(array))
print("Expected: " + str(result))
print("Output: " + str(product_except_itself_1(array)))
