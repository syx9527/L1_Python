s1 = input()
s2 = input()

if len(s2) > len(s1):
    s1, s2 = s2, s1
len1 = len(s1)
len2 = len(s2)
xmax = 0
xindex = 0
matrix = [[0] * len1 for i in range(len2)]
for i, x in enumerate(s2):
    for j, y in enumerate(s1):
        if x == y:
            if i == 0 or j == 0:
                matrix[i][j] = 1
            else:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            if matrix[i][j] > xmax:
                xmax = matrix[i][j]
                xindex = j
print(s1[xindex - xmax + 1:xindex + 1])
