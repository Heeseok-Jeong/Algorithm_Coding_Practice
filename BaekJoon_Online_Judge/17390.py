import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
A = [0] + list(map(int, input().split()))
questions = [list(map(int, input().split())) for _ in range(Q)]

A.sort()
sum_A = A
for i in range(1, N+1):
    sum_A[i] = sum_A[i] + sum_A[i-1]

for L, R in questions:
    print(sum_A[R] - sum_A[L-1])
