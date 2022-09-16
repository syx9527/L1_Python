"""
a=100
b=200
"""
a = input().split("=")
b = input().split("=")
print(f"""{a[0]}={b[1]}
{b[0]}={a[1]}""")
