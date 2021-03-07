def frac(x):
    if x <= 1:
        return 1
    
    return x * frac(x-1)


N, K = map(int, input().split())
print(frac(N) // (frac(K) * frac(N-K)))
