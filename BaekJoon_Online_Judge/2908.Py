import sys

a, b = sys.stdin.readline().split()
new_a = ""
new_b = ""

for i in range(2, -1, -1):
    new_a += a[i]
    new_b += b[i]

new_a = int(new_a)
new_b = int(new_b)

if new_a > new_b:
    print(new_a)
else:
    print(new_b)
