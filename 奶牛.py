s = input().split(" ")
s = [int(i) for i in s]
N = s[0]
S = s[1]
n = []
for i in range(N):
    n.append(int(input()))

res = 0
for i in range(N - 1):
    for j in range(i+1,N):
        if n[i]+n[j]<=S:
            res+=1
print(res)
