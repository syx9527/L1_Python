"""
描述

NIT曾经做过一道签到题：输入a和b，输出任意一个的a倍数c，并且保证b是c的倍数（a<c<b）

NIT觉得这样的题太简单，于是加强了这道题目：

输入四个数a，b，c，d，请你输入一个正整数x，满足x是a的倍数且x是c的倍数，另外

满足b是x的倍数且d是x的倍数。（要求：a<x<b,c<x<d）


输入
四个正整数：a,b,c,d

（1<=a<b<=10^9，1<=c<d<=10^9）


输出
如果存在合法解，请输入任意一个合法解。

否则输出-1


输入样例 1

2 60 3 96
输出样例 1

12
输入样例 2

2 60 3 81
输出样例 2

-1
"""


def get_LCM(x: int, y: int) -> int:
    """
    :return: x, y最小公倍数
    """
    if x > y:
        x, y = y, x
    temp = 1
    for i in range(x, 1, -1):
        if x % i == 0 and y % i == 0:
            temp = i
            break
    return (x * y) // temp


def get_GCD(x: int, y: int) -> int:
    """
    :return: x, y最大公因数
    """
    temp = 1
    for i in range(x, 1, -1):
        if x % i == 0 and y % i == 0:
            temp = i
            break
    return temp


a, b, c, d = tuple(map(int, input().split(" ")))
lcm = get_LCM(a, c)
gcd = get_GCD(b, d)

if gcd % lcm == 0:
    print(gcd)
else:
    print(-1)
