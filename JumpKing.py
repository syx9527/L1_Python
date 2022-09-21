s = [int(i) for i in input().split(" ")]
n = s[0]
s = s[1:]
l = list(range(1, n))
_l = []
for i in range(len(s) - 1):
    _l.append(abs(s[i] - s[i + 1]))
_l.sort()
if l == _l:
    print("JumpKing")
else:
    print("NotJumpKing")
