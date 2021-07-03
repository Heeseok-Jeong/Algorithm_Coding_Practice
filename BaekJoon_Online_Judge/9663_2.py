from copy import deepcopy

N = int(input())
answer = 0

def browse(q_arr, row):
    # print(q_arr)
    global answer
    if row == N:
        answer += 1
        return
    
    for col in range(N):
        avail = True
        for q_row, q_col in q_arr:
            if col == q_col or (abs(row-q_row) == abs(col-q_col)):
                avail = False
                break
        if avail:
            q_arr.append((row, col))
            browse(deepcopy(q_arr), row+1)
            q_arr.pop()

for s in range(N):
    browse([(0, s)], 1)
print(answer)
