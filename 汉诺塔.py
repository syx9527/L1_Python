def hanno(n, a, b, c):
    if n > 0:
        hanno(n - 1, a, c, b)
        print(f"{a}->{c}")
        hanno(n - 1, b, a, c)


n = int(input())
hanno(n, 'a', 'b', 'c')
