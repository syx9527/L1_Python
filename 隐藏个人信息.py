
data = input()
data = data.split("@")
if len(data) == 1:

    data = data[0]
    res = data[:3] + "*" * 6 + data[-2:]
    print(res)
elif len(data) == 2:
    name = data[0].lower()
    com = data[1].lower()
    name = name[0] + "*" * 5 + name[-1]
    res = name + "@" + com
    print(res)

