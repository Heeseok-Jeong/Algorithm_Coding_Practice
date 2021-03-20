def z(n, x, y):
    global result, N, flag
    if x == r and y == c:
        flag = True
        return
    if flag:
        return
    
    if n == 0:
        result += 1
    elif not (x <= r < x+2**n and y <= c < y+2**n) and n != N:
        result += 4**n
    else:    
        z(n-1, x, y)
        z(n-1, x, y + 2**(n-1))
        z(n-1, x + 2**(n-1), y)
        z(n-1, x + 2**(n-1), y + 2**(n-1))

N, r, c = map(int, input().split())
result = 0
flag = False
z(N, 0, 0)
print(result)
