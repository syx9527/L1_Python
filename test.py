import random


def is_ugly(a):
    while True:
        if a == 1:
            # print("true")
            return "true"
        else:
            if a % 2 == 0:
                a = a // 2
            elif a % 3 == 0:
                a = a // 3
            elif a % 5 == 0:
                a = a // 5
            else:
                return "false"


if __name__ == "__main__":

    test_data = [random.randint(2, 6587) for _ in range(3)]
    # n = int(input())
    # is_ugly(n)
    for i in range(2):
        test_data.append(2 ** random.randint(0, 3) * 3 ** random.randint(0, 3) * 5 ** random.randint(0, 3))
    test_data.sort()
    out_data = [is_ugly(i) for i in test_data]
    print(test_data)
    print(out_data)
    print("hello world")
