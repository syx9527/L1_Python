n = int(input())

i = 0
while n > 0:
    n -= 2 * 0.95 ** i
    i += 1
print(i)
