A, B = map(int, input().split())

seq = [0] * (B+1)

count = 0
pivot = 1
for i in range(1, B+1):
    count += 1
    
    if count <= pivot:
        seq[i] = pivot
        if count == pivot:
            pivot += 1
            count = 0

print(sum(seq[A:B+1]))
