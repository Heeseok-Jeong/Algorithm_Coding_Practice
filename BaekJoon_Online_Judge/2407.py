def fac(x):
    if x == 1:
        return x
    
    return x * fac(x-1)

n, m = map(int, input().split())
result = fac(n) // (fac(m) * fac(n-m))

print(result)
