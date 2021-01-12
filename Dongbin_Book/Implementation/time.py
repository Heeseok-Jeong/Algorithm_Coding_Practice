n = int(input())

h = 0
m = 0
s = 0
answer = 0

while h <= n:
    s += 1
    if s == 60:
        m += 1
        s = 0
    if m == 60:
        h += 1
        m = 0

    if '3' in str(h)+str(m)+str(s):
        answer += 1

# for h in range(n+1):


print(answer)
