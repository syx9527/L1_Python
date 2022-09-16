"""
hello,helloworld,he,hao,good,bad,world
"""
s = input().split(",")
s.sort(key=lambda i: len(i), reverse=True)
print(",".join(s))
