n = int(input())
res = []
for i in range(n):
    temp = input()
    l = len(temp)
    for j in range(len(temp) - 1):
        if temp[j] == temp[j + 1]:
            l += 1
    res.append(l)

for i in res:
    print(i)
