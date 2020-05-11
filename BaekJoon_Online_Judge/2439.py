import sys

n = int(sys.stdin.readline())
sp = " "
st = "*"


for i in range(1, n+1):
    a = ""
    b = ""
    for j in range(n-i, 0, -1):
        a += sp

    for k in range(1, i+1):
        b += st
    print(a+b)
