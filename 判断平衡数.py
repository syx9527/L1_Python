def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result


input_nums = [int(i) for i in input()]

for i in range(1, len(input_nums)):
    if multiplyList(input_nums[:i]) == multiplyList(input_nums[i:]):
        print("YES")
        break
else:
    print("NO")
