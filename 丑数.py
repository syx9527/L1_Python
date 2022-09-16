def is_ugly(a):
    while True:
        if a == 1:
            print("true")
            return
        elif a == -1:
            print("false")
            return
        else:
            if a % 2 == 0:
                a = a // 2
            elif a % 3 == 0:
                a = a // 3
            elif a % 5 == 0:
                a = a // 5
            else:
                a = -1


n = int(input())
is_ugly(n)
