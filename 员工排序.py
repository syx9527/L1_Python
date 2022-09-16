"""
6
张三 3 3 3000
李四 3 4 3000
王五 3 3 4000
赵六 4 3 3000
陆奇 4 4 4000
闫八 4 4 3980.99
"""

n = int(input())
p = []
for i in range(n):
    _ = input().strip().split(" ")
    p.append([_[0], int(_[1]), int(_[2]), float(_[3])])
p.sort(key=lambda x: (-x[1], x[3], -x[2]))

for _ in p:
    print('%s %d %d %.2f' % (_[0], _[1], _[2], _[3]))
