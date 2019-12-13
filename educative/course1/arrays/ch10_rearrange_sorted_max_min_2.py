array = [1,2,3,4,5]
result = [5,1,4,2,3]


# in-place replacement
def rearrange_sorted_max_min_2(arr):
    max_index = len(arr) - 1
    min_index = 0
    max_elem = arr[max_index] + 1

    # orig element of stored as remainder, max or min element stored
    # as multiplier, this allows to swap numbers in place, finally
    # divide each element by max element to get output array
    for i in range(len(arr)):
        if i%2 is 0:
            arr[i] += (arr[max_index] % max_elem) * max_elem
            max_index -= 1
        else:
            arr[i] += (arr[min_index] % max_elem) * max_elem
            min_index += 1

    for i in range(len(arr)):
        arr[i] = arr[i] // max_elem

    return arr


def main():
    print("Input: " + str(array))
    print("Expected: " + str(result))
    print("Output: " + str(rearrange_sorted_max_min_2(array)))


if __name__ == '__main__':
    main()
