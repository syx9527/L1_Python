"""
水仙花数
描述

如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数


输入
输入一个整数 a 与一个整数 b, 用空格分隔


输出
输出 a 到 b 区间内的水仙花数
"""

data = input().strip().split(" ")
a = int(data[0])

b = int(data[1])
res = []
for i in range(a, b + 1):
    if (i // 100) ** 3 + (i // 10 % 10) ** 3 + (i % 10) ** 3 == i:
        res.append(i)
print(" ".join(map(str, res)))
