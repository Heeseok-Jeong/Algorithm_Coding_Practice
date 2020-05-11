import sys

n, x = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = ""

for i in a:
    if i < x:
        b += str(i) + " "
print(b)
