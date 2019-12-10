array = [1, 21, 3, 14, 5, 60, 7, 6]
n = 27
result = "[21, 6] or [6, 21]"


# iterate both arrays in a nested loop, check for sum == n, return when pair is found

def add_upto_n_1(arr, n):
    output = []

    for x in arr:
        for y in arr:
            if x + y == n:
                output.append(x)
                output.append(y)
                return output

    return None


print("Input: " + "array = " + str(array) + ", " + "n = " + str(n))
print("Expected: " + str(result))
print("Output: " + str(add_upto_n_1(array, n)))
