N, X = map(int, input().split())

if X > 26*N or N > X:
    print("!")
else:
    q = (X-N) // (26-1)
    a_num, other_num = 0, 0

    if X != 26*N:
        a_num = N-q-1
        other_num = 1
        
    print("A" * a_num + chr(64 + (X- 26*q - (N-q-1))) * other_num + "Z" * q)
