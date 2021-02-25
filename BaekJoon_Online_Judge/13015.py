N = int(input())

answer = [""]
for i in range(1, 2*N):
    if i == 1:
        answer.append("*"*N + " "*(4*N-3 - 2*N) + "*"*N)
    elif i < N:
        answer.append(" "*(i-1) + "*" + " "*(N-2) + "*" + " "*(4*N-3 - 2*(N+i-1)) + "*" + " "*(N-2) + "*")
    elif i == N:
        answer.append(" "*(i-1) + "*" + " "*(N-2) + "*" + " "*(N-2) + "*")
    elif i > N:
        answer.append(answer[2*N-i])

for i in range(1, 2*N):
    print(answer[i])
