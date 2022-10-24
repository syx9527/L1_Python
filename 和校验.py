s = []
while True:
    temp = input().strip()
    if temp == "#":
        break
    else:
        s.append(temp)

for i in s:
    res = 0
    for j in range(len(i)):
        if i[j] != ' ':
            res += (ord(i[j]) - 64) * (j + 1)

    print(res)
