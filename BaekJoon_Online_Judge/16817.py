A, B, C, X, Y = map(int, input().split())

answer = 0
if not (A + B > 2*C):
    answer = A*X + B*Y
else:
    minimum = min(X, Y)
    
    answer = 2*C*minimum

    if (X-minimum) == 0:
        if 2*C < B:
            answer += (Y-minimum)*2*C
        else:
            answer += (Y-minimum)*B
    else:
        if 2*C < A:
            answer += (X-minimum)*2*C
        else:
            answer += (X-minimum)*A

print(answer)
