import sys

n = int(sys.stdin.readline())

for i in range(n, 0, -1):
    str =""
    for j in range(0, n-i):
        str += " "
    for j in range(1, 2*i):
        str += "*"
    print(str)

for i in range(2, n+1):
    str =""
    for j in range(0, n-i):
        str += " "
    for j in range(1, 2*i):
        str += "*"
    print(str)
