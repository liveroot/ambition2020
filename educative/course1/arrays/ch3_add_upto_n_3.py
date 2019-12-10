array = [1, 21, 3, 14, 5, 60, 7, 6]
n = 27
result = "[21, 6] or [6, 21]"


# if n-x in set, implies x is the other number

def add_upto_n_3(arr, n):
    output = []

    x = 0
    temp = set()

    for x in arr:
        if n - x in temp:
            output.append(x)
            output.append(n - x)
        else:
            temp.add(x)

    return output


print("Input: " + "array = " + str(array) + ", " + "n = " + str(n))
print("Expected: " + str(result))
print("Output: " + str(add_upto_n_3(array, n)))
