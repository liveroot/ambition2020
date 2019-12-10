array = [1, 21, 3, 14, 5, 60, 7, 6]
n = 27
result = "[21, 6] or [6, 21]"


# step1: sort
# step2: use 2 indices, one at start, one at end,
# increment fist if sum < n, decrement second if sum > n, return if sum == n

def add_upto_n_2(arr, n):
    output = []
    i = 0
    j = len(arr) - 1

    arr.sort()

    while i != j:
        if arr[i] + arr[j] < n:
            i += 1
        elif arr[i] + arr[j] > n:
            j -= 1
        else:
            output.append(arr[i])
            output.append(arr[j])
            return output

    return None


print("Input: " + "array = " + str(array) + ", " + "n = " + str(n))
print("Expected: " + str(result))
print("Output: " + str(add_upto_n_2(array, n)))
