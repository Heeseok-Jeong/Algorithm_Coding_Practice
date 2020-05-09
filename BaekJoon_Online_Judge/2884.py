a, b = map(int, input().split())

if b < 45:
    c = a-1
    if c < 0:
        c = 23
    d = b-45
    if d < 0:
        d = 60-abs(d)
else:
    c = a
    d = b-45


print(c,d)
