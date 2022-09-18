n = int(input())
c = list()

for i in range(n):
    c.append(input())

m = int(input())
l = list()
for i in range(m):
    l.append(input())

for i in l:
    for j in c:

        if j in i:
            print("Congratulations!Welcome to S.H.I.E.L.D!")
            break
    else:
        print("Sorry!You're eliminated!")
