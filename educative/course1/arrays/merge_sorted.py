array1 = [1, 3, 4, 5]
array2 = [2, 6, 7, 8]
result = [1, 2, 3, 4, 5, 6, 7, 8]


def merge_sorted(arr1, arr2):
    output = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            output.append(arr1[i])
            i += 1
        else:
            output.append(arr2[j])
            j += 1

    while i < len(arr1):
        output.append(arr1[i])
        i += 1

    while j < len(arr2):
        output.append(arr2[j])
        j += 1

    return output


print("Input: " + str(array1) + ", " + str(array2))
print("Expected: " + str(result))
print("Output: " + str(merge_sorted(array1, array2)))
