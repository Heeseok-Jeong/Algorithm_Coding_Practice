import sys

a = sys.stdin.readline().strip()
count = 0

for i in range(0, len(a)):
    if a[i] == '-':
        if a[i-1] == 'c' or a[i-1] == 'd':
            continue
        else:
            count += 1
    elif a[i] == 'j':
        if a[i-1] == 'l' or a[i-1] == 'n':
            continue
        else:
            count += 1
    elif a[i] == '=' and a[i-1] == 'z' and a[i-2] == 'd':
        count -= 1
        continue
    elif a[i] == '=' and a[i-1] == 'z':
        continue
    elif a[i] == '=':
        if a[i-1] == 'c' or a[i-1] == 's':
            continue
        else:
            count += 1
    else:
        count += 1

print(count)
