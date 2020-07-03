import sys

n, m = map(int, sys.stdin.readline().split())
result = []

def solve(depth, n, m):
  if depth == m:
    print(" ".join(map(str, result)))
    return
  for i in range(1, n+1):
    result.append(i)
    solve(depth+1, n, m)
    result.pop()

solve(0, n, m)
