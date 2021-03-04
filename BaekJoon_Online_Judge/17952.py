N = int(input())

scores = [0] * (N+1)
left_time = [-1] * (N+1)
assignment_stack = []
current_index = 0
total_score = 0

def do_assignment():
    global total_score, current_index
    left_time[current_index] -= 1

    if left_time[current_index] == 0:
        total_score += scores[current_index]
        current_index = assignment_stack.pop() if assignment_stack else 0
        
for i in range(1, N+1):
    info = list(map(int, input().split()))
    
    if info[0] == 0:
        if current_index != 0:
            do_assignment()
    elif info[0] == 1:
        _, A, T = info

        if current_index != 0:
            assignment_stack.append(current_index)
        
        current_index = i
        scores[current_index] = A
        left_time[current_index] = T
        do_assignment()

print(total_score)
