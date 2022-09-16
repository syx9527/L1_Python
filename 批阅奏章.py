p, q = list(map(int, input().split(' ')))
P = list(map(int, input().split(' ')))
Q = list(map(int, input().split(' ')))
RES = []
for i in Q:
    cnt = P.count(i)
    RES.extend([i] * cnt)
    while i in P:
        P.remove(i)
P.sort()
RES.extend(P)
print(' '.join(list(map(str, RES))))
