def pisano(n: int) -> list:
    l = [0, 1, ]
    if n < 2:
        return l[:n]
    else:
        l = l + [0 for _ in range(n - 2)]
        for i in range(2, n):
            l[i] = l[i - 1] + l[i - 2]
        return l


if __name__ == '__main__':
    n = int(input())
    res = map(str, pisano(n))
    print(" ".join(res))
