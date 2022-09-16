def lastRemaining(n: int) -> int:
    base = 1
    res = 1
    while (base * 2 <= n):
        res += base
        base *= 2
        if (base * 2 > n):
            break
        if (int((n / base)) % 2 == 1):
            res += base
        base *= 2
    return res


n = int(input())

print(lastRemaining(n))
