import math

e = 2.7182818284590452354
pai = 3.141592653589793239


def pa(n):
    if n < 2:
        return 1
    o = math.log10(2 * pai * n) * 0.5 + n * math.log10(n / e) + 1
    return int(o)


m = int(input())
data = []
for i in range(m):
    data.append(int(input()))
for _ in data:
    print(pa(_))
