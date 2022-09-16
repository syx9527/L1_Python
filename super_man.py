"""
2
A
T
4
ACA
TAC
AGT
YHG
"""

n = int(input())
c = set()

for i in range(n):
    c.add(input())

m = int(input())
l = list()
for i in range(m):
    l.append(input())

for i in range(m):
    if c & set(l[i]):
        print("ok")
    else:
        print("no")