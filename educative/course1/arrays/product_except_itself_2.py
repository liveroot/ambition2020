array = [1,2,3,4]
result = [24,12,8,6]


def product_except_itself_2(nums):
    output = []

    L = []
    R = []

    temp = 1
    for x in nums:
        L.append(temp)
        temp = temp * x

    temp = 1
    for y in nums[::-1]:
        R.append(temp)
        temp = temp * y

    for i in range(len(R)):
        output.append(L[i]*R[len(R)-1-i])

    return output


print("Input: " + str(array))
print("Expected: " + str(result))
print("Output: " + str(product_except_itself_2(array)))
