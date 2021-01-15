n, m = map(int, input().split())
ddeok = list(map(int, input().split()))

ddeok.sort()
s = 0
e = ddeok[n-1]
height = 0
while s <= e:
    mid = (s + e) // 2
    cut = 0
    for x in ddeok:
        if x > mid:
            cut += x - mid
    if cut < m:
        e = mid - 1
    else:
        height = mid
        s = mid + 1

print(height)
