"""
hello word
"""
s = input()
s = s.split(" ")
max_length = 0
for i in s:
    if len(i) > max_length:
        max_length = len(i)
data = []
for i in range(max_length):
    temp = ""
    for _ in s:
        if len(_) > i:
            c = _[i]
        else:
            c = " "
        temp += c
    data.append(temp)
print(data)
for i in data:
    print(i)
