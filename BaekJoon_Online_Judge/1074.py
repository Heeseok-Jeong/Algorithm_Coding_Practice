n, r, c = map(int, input().split())

result = 0
flag = False

def z(n, x, y):
    global result, flag
    if flag:
        return

    if x == r and y == c:
        flag = True
    elif n == 1:
        result += 1
    elif not (x <= r < x + n and y <= c < y + n):
        result += n**2
    else:    
        z(n / 2, x, y)
        z(n / 2, x, y + n/2)
        z(n / 2, x + n/2, y)
        z(n / 2, x + n/2, y + n/2)

z(2**n, 0, 0)
print(int(result))
