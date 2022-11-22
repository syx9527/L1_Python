
"""
不知道是题目还是代码边界问题没有解决，通过率 80%
"""



m = int(input())
data = []
for i in range(m):
    data.append(list(map(int, input().strip().split(" "))))
res = []

for i in data:
    if i[2] < 41:
        res.append(i[0] * i[1] * i[2])
if res:
    for i in res:
        print(i)
else:
    print(0)
