def parse(numbers: list, sum_number: int) -> tuple or None:
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == sum_number:
                return numbers[i], numbers[j]
            elif numbers[i] + numbers[j] > sum_number:
                break


if __name__ == '__main__':
    inputs = list(map(int, input().strip().split(" ")))
    res = int(input())
    inputs.sort()
    a, b = parse(inputs, res)
    print(a, b)
