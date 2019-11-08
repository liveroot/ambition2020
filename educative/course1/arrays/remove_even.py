array = [1, 2, 4, 5, 10, 6, 3]
result = [1, 5, 3]


def remove_even(arr):
    numodds = 0
    output = []

    for x in arr:
        if x % 2 != 0:
            numodds += 1

    if numodds > 0:
        for x in arr:
            if x % 2 != 0:
                output.append(x)
    else:
        output = "no odds found"

    return output


print("Input: " + str(array))
print("Expected: " + str(result))
print("Output: " + str(remove_even(array)))
