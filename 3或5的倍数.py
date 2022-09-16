n = int(input())
res = 0
for i in range(n):
    if i % 3 == 0 or i % 5 == 0:
        res += i
print(res)
