import sys

sum = 0
for i in range(0, 5):
    a = int(sys.stdin.readline())
    if a < 40:
        a = 40
    sum += a
n = 5

print(sum//n)
