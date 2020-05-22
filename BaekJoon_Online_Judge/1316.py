import sys

n = int(sys.stdin.readline())
count = 0

for i in range(0, n):
    a = sys.stdin.readline().strip()
    b = []
    index = -1
    if len(a) == 1:
        count += 1
    else: 
        for j in range(0, len(a)):
            if a[j] not in b:
                b.append(a[j])
            elif a[j] in b and a[j] == a[j-1]:
                continue
            elif a[j] in b and a[j] != a[j-1]:
                count -= 1
                break
        count += 1

print(count)
