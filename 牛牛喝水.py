input_data = input().split(' ')
h = int(input_data[0])
r = int(input_data[1])
v = 3.14 * h * r * r

n = int(10000 / v)

if (10 / v) % 1 != 0:
    n += 1

print(n)
